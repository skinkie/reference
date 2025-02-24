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

    def open_table(self, klass: T):
        name: str = get_object_name(klass)
        if name in self.dbs:
            return self.dbs[name]
        else:
            name_bytes = name.encode('utf-8')
            try:
                # Try opening in read-only mode first to isolate the issue
                db = self.lmdb.open_db(name_bytes)
            except lmdb.Error as e:
                if "MDB_NOTFOUND" in str(e):
                    print(f"Database {name} does not exist, creating it.")
                    db = self.lmdb.open_db(name_bytes, create=True)
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
        self.lmdb = lmdb.open(self.database_file, map_size=MAP_SIZE, max_dbs=len(self.serializer.name_object), readonly=self.read_only)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.lmdb.close()

    def clear_tables(self, classes: list[Type[T]]):
        dbs = [self.open_table(klass) for klass in classes]
        with self.lmdb.begin(write=True) as txn:
            for db in dbs:
                txn.drop(db, delete=False)

    def insert_one_object(self, object, quiet=False):
        return self.insert_many_objects(object.__class__, [object], quiet)

    def insert_many_objects(self, klass: T, objects: Iterator, quiet=False):
        objectname: str = get_object_name(klass)
        now = time.time()

        i = 0
        with self.lmdb.begin(write=True, db=self.open_table(klass)) as txn:
            for object in objects:
                key = (object.id, object.version)
                # TODO: do something with "now"
                value = self.serializer.marshall(object, klass)
                txn.put(pickle.dumps(key), value)
                if not quiet and i % 13 == 0:
                    print('\r', objectname, str(i), end='')
                i += 1

        if not quiet:
            print('\r', objectname, str(i), end='\n')

    def vacuum(self):
        if self.lmdb:
            tmp_file = self.database_file + "_compacted.mdb"
            self.lmdb.copy(path=tmp_file, compact=True)
            self.lmdb.close()
            os.rename(tmp_file, self.database_file)
            self.lmdb = lmdb.open(self.database_file, map_size=MAP_SIZE, max_dbs=len(self.serializer.name_object), readonly=self.read_only)

    def tables(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.lmdb:
            # Try to open each database by index, starting from 0 up to max_dbs
            tables = set([])
            with self.lmdb.begin() as txn:
                cursor = txn.cursor()
                for key, _ in cursor:
                    name = key.decode('utf-8')
                    if name[0] != '_':
                        tables.add(self.get_class_by_name(name))
            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def referencing(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.lmdb:
            tables = set([])
            with self.lmdb.begin(write=False, db=self.lmdb.open_db(b'_referencing', readonly=True)) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _ref, _version = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def embedded(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.lmdb:
            tables = set([])
            with self.lmdb.begin(write=False, db=self.lmdb.open_db(b'_embedded', readonly=True)) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _id, _version, _order, _path = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def get_class_by_name(self, name: str):
        return self.serializer.name_object[name]
