import os
import pickle
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

    def copy_db(self, target: Database, klass: T, batch_size=100_000, max_mem=4 * 1024 ** 3):
        """
        Copies a single database from `src_env` to `dst_env` with high throughput.

        - `src_env`: Source LMDB environment
        - `dst_env`: Destination LMDB environment
        - `db_name`: Database name (bytes)
        - `batch_size`: Number of records per transaction commit
        - `max_mem`: Max memory usage before commit (default: 4GB)
        """

        src_db = self.open_db(klass)
        dst_db = target.open_db(klass)

        total_size = 0  # Track memory usage
        batch = []

        with self.env.begin(db=src_db, readonly=True) as src_txn:
            with target.env.begin(write=True, db=dst_db) as dst_txn:
                cursor = src_txn.cursor()

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

    def copy_db_embedding(self, target: Database, classes: list[T], batch_size=100_000, max_mem=4 * 1024 ** 3):
        """
        Copies '_referencing' and '_embedding' databases from `self.env` to `target.env` with high throughput.

        - `batch_size`: Number of records per transaction commit
        - `max_mem`: Max memory usage before commit (default: 4GB)
        """
        classes_name = {get_object_name(klass) for klass in classes}

        def _copy_db(db_name: bytes):
            """ Helper function to copy data between LMDB databases efficiently. """
            src_db = self.env.open_db(db_name, readonly=True)
            dst_db = target.env.open_db(db_name, readonly=False)

            total_size = 0  # Track memory usage
            batch = []

            with self.env.begin(db=src_db, readonly=True) as src_txn:
                with target.env.begin(write=True, db=dst_db) as dst_txn:
                    cursor = src_txn.cursor()

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

    def open_db(self, klass: T):
        name: str = get_object_name(klass)
        if name in self.dbs:
            return self.dbs[name]
        else:
            name_bytes = name.encode('utf-8')
            try:
                # Try opening in read-only mode first to isolate the issue
                db = self.env.open_db(name_bytes)
            except lmdb.Error as e:
                if "MDB_NOTFOUND" in str(e):
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
        self.env.close()

    def clear_tables(self, classes: list[Type[T]]):
        dbs = [self.open_db(klass) for klass in classes]
        with self.env.begin(write=True) as txn:
            for db in dbs:
                txn.drop(db, delete=False)

    def insert_one_object(self, object, quiet=False):
        return self.insert_many_objects(object.__class__, [object], quiet)

    def insert_many_objects(self, klass: T, objects: Iterator, batch_size=100_000, quiet=False):
        """ Inserts multiple objects into LMDB with batch processing. """
        objectname: str = get_object_name(klass)
        db = self.open_db(klass)
        now = time.time()

        batch = []
        i = 0

        with self.env.begin(write=True, db=db) as txn:
            for obj in objects:
                key = pickle.dumps((obj.id, obj.version))
                # TODO: do something with "now"
                value = self.serializer.marshall(obj, klass)
                batch.append((key, value))

                if not quiet and i % 13 == 0:
                    print('\r', objectname, str(i), end='')

                if len(batch) >= batch_size:
                    for k, v in batch:
                        txn.put(k, v)
                    txn.commit()  # Commit batch
                    txn = self.env.begin(write=True, db=db)  # Start new transaction
                    batch.clear()

                i += 1

            # Final commit for remaining objects
            if batch:
                for k, v in batch:
                    txn.put(k, v)
                txn.commit()

        if not quiet:
            print('\r', objectname, str(i), end='\n')

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
            with self.env.begin(write=False, db=self.env.open_db(b'_referencing', readonly=True)) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _ref, _version = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def embedded(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            tables = set([])
            with self.env.begin(write=False, db=self.env.open_db(b'_embedded', readonly=True)) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _id, _version, _order, _path = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def get_class_by_name(self, name: str):
        return self.serializer.name_object[name]
