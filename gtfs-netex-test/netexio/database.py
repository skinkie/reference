from __future__ import annotations

import os
import pickle
import queue
import threading
from logging import Logger
from typing import Generator, Iterator, Type, TypeVar
T = TypeVar("T")

import lmdb
import time

from netexio.serializer import Serializer
from utils import get_object_name

MAP_SIZE = (10 ** 9) * 32

class Database:
    database_file: str
    read_only: bool
    serializer: Serializer
    object_cache: dict

    def __init__(self, database_file: str, serializer: Serializer, read_only: bool=True, logger: Logger=None):
        self.database_file = database_file
        self.read_only = read_only
        self.logger = logger
        self.serializer = serializer

        self.object_cache = {}
        self.dbs = {}

        self.task_queue = None  # Shared queue for writing tasks
        self.writer_thread = None
        self.stop_signal = object()  # Unique object to signal termination
        self.lock = threading.Lock()  # Ensure only one writer thread runs

    def start_writer_if_needed(self, batch_size=1_000, max_mem=4 * 1024 ** 3):
        """ Starts the writer thread if it's not already running. """
        with self.lock:
            if self.task_queue is None:
                self.task_queue = queue.Queue(maxsize=1000)  # Shared queue
                self.writer_thread = threading.Thread(
                    target=self.writer,
                    args=(batch_size, max_mem),
                    daemon=True
                )
                self.writer_thread.start()

    def insert_object_on_queue(self, klass, objects, batch_size=100_000, max_mem=4 * 1024 ** 3):
        """ Places objects in the shared queue for writing, starting writer if needed. """
        db_handle = self.open_db(klass)
        self.start_writer_if_needed(batch_size, max_mem)

        # total_size = 0
        for obj in objects:
            version = obj.version if hasattr(obj, 'version') else None
            key = pickle.dumps((obj.id, version))
            value = self.serializer.marshall(obj, klass)
            item_size = len(key) + len(value)

            self.task_queue.put((db_handle, key, value))
            # total_size += item_size

            # if total_size >= max_mem:
            #     self.task_queue.put(self.stop_signal)  # Force commit
            #    total_size = 0  # Reset memory counter

    def writer(self, batch_size=100_000, max_mem=4 * 1024 ** 3):
        """ Writes data from the queue to LMDB in batches. """
        while True:
            batch = []
            total_size = 0

            try:
                for _ in range(batch_size):
                    item = self.task_queue.get(timeout=3) # TODO reduce back to 3
                    if item is self.stop_signal:
                        # self.task_queue.put(self.stop_signal)  # Ensure stop is propagated
                        break
                    batch.append(item)
                    total_size += len(item[1]) + len(item[2])  # Key + Value size

                    if total_size >= max_mem:
                        break  # Commit early if memory limit is reached

            except queue.Empty:
                pass
                # if not batch:
                #    break  # Stop if queue remains empty

            if batch:
                with self.env.begin(write=True) as txn:
                    for db_handle, key, value in batch:
                            txn.put(key, value, db=db_handle)

            if item is self.stop_signal:
                break

        # Cleanup after writing is done
        with self.lock:
            self.task_queue = None
            self.writer_thread = None

    def insert_many_objects(self, klass, objects, batch_size=1_000, max_mem=4 * 1024 ** 3, quiet=False, block=False):
        """ Wrapper around insert_object_on_queue to ensure objects are written in batch. """
        self.insert_object_on_queue(klass, objects, batch_size, max_mem)

        if block:
            if not quiet:
                print(f"Insertion of {get_object_name(klass)} objects started.")

            self.block_until_done()

            if not quiet:
                print(f"Insertion of {get_object_name(klass)} objects completed.")

    def block_until_done(self):
        if self.writer_thread:
            self.task_queue.put(self.stop_signal)
            self.writer_thread.join() # Wait for writer to finish

    def copy_db(self, target: Database, klass: T, batch_size=1_000, max_mem=4 * 1024 ** 3):
        """
        Copies a single database from `src_env` to `dst_env` with high throughput.

        - `src_env`: Source LMDB environment
        - `dst_env`: Destination LMDB environment
        - `db_name`: Database name (bytes)
        - `batch_size`: Number of records per transaction commit
        - `max_mem`: Max memory usage before commit (default: 4GB)
        """

        src_db = self.open_db(klass, readonly=True)
        if src_db is None:
            return

        dst_db = target.open_db(klass)

        total_size = 0  # Track memory usage
        batch = []

        with self.env.begin(db=src_db, write=False) as src_txn:
            cursor = src_txn.cursor()
            dst_txn = target.env.begin(write=True, db=dst_db)  # Open initial write transaction

            for key, value in cursor:
                batch.append((key, value))
                total_size += len(key) + len(value)

                if len(batch) >= batch_size or total_size >= max_mem:
                    for k, v in batch:
                        dst_txn.put(k, v)

                    dst_txn.commit()  # Commit batch
                    dst_txn = target.env.begin(write=True, db=dst_db)  # Start new txn

                    batch.clear()
                    total_size = 0  # Reset memory counter

            # Final commit for remaining records
            if batch:
                for k, v in batch:
                    dst_txn.put(k, v)
                dst_txn.commit()

    def copy_db_embedding(self, target: Database, classes: list[T], batch_size=1_000, max_mem=4 * 1024 ** 3):
        """
        Copies '_referencing' and '_embedding' databases from `self.env` to `target.env` with high throughput.

        - `batch_size`: Number of records per transaction commit
        - `max_mem`: Max memory usage before commit (default: 4GB)
        """
        classes_name = {get_object_name(klass) for klass in classes}

        def _copy_db(db_name: bytes):
            """ Helper function to copy data between LMDB databases efficiently. """
            src_db = self.env.open_db(db_name)
            dst_db = target.env.open_db(db_name)

            total_size = 0  # Track memory usage
            batch = []

            with self.env.begin(write=False, db=src_db) as src_txn:
                cursor = src_txn.cursor()
                dst_txn = target.env.begin(write=True, db=dst_db)  # Open initial write transaction

                for key, value in cursor:
                    parent_class, *_ = pickle.loads(key)
                    if parent_class not in classes_name:
                        continue

                    batch.append((key, value))
                    total_size += len(key) + len(value)

                    if len(batch) >= batch_size or total_size >= max_mem:
                        for k, v in batch:
                            dst_txn.put(k, v)

                        dst_txn.commit()  # Commit batch
                        dst_txn = target.env.begin(write=True, db=dst_db)  # Start new txn

                        batch.clear()
                        total_size = 0  # Reset memory counter

                # Final commit for remaining records
                if batch:
                    for k, v in batch:
                        dst_txn.put(k, v)
                    dst_txn.commit()

        # Copy both databases
        _copy_db(b'_referencing')
        _copy_db(b'_embedding')

    def open_db(self, klass: T, readonly=False):
        name: str = get_object_name(klass)
        if name in self.dbs:
            return self.dbs[name]
        else:
            name_bytes = name.encode('utf-8')
            try:
                # Try opening in read-only mode first to isolate the issue
                db = self.env.open_db(name_bytes, create=False)
            except lmdb.Error as e:
                if "MDB_NOTFOUND" in str(e):
                    if readonly:
                        return None
                    print(f"Database {name} does not exist, creating it.")
                    db = self.env.open_db(name_bytes, create=True)
                else:
                    raise  # Reraise other LMDB errors
            except Exception as ex:
                print(f"Unexpected error: {ex}")
                raise

            self.dbs[name] = db
            return db

    def cursor(self):
        return self.con.cursor()

    def clean_cache(self):
        self.object_cache = {}

    def __enter__(self):
        self.env = lmdb.open(self.database_file, map_size=MAP_SIZE, max_dbs=len(self.serializer.name_object), readonly=self.read_only)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.block_until_done()
        self.env.close()

    def clear_tables(self, classes: list[Type[T]]):
        dbs = [self.open_db(klass) for klass in classes]
        with self.env.begin(write=True) as txn:
            for db in dbs:
                txn.drop(db, delete=False)

    def insert_one_object(self, object, quiet=False):
        return self.insert_many_objects(object.__class__, [object], quiet=quiet)

    def vacuum(self):
        if self.env:
            tmp_file = self.database_file + "_compacted.mdb"
            self.env.copy(path=tmp_file, compact=True)
            self.env.close()
            os.rename(tmp_file, self.database_file)
            self.env = lmdb.open(self.database_file, map_size=MAP_SIZE, max_dbs=len(self.serializer.name_object), readonly=self.read_only)

    def tables(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            # Try to open each database by index, starting from 0 up to max_dbs
            tables = set([])
            with self.env.begin() as txn:
                cursor = txn.cursor()
                for key, _ in cursor:
                    name = key.decode('utf-8')
                    if name[0] != '_':
                        tables.add(self.get_class_by_name(name))
            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def referencing(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            tables = set([])
            with self.env.begin(write=False, db=self.env.open_db(b'_referencing')) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    klass, *_ = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def embedded(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            tables = set([])
            with self.env.begin(write=False, db=self.env.open_db(b'_embedded')) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _id, _version, _order, _path = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def get_class_by_name(self, name: str):
        return self.serializer.name_object[name]
