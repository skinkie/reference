import os
import pickle
from logging import Logger
from typing import T

import duckdb
import lmdb

from netexio.pickleserializer import MyPickleSerializer
from netexio.serializer import Serializer
from utils import get_object_name
from vdvserver.generic import serializer


class Database:
    database_file: str
    read_only: bool
    serializer: Serializer
    con: duckdb.DuckDBPyConnection
    object_cache: dict

    def __init__(self, database_file: str, read_only: bool=True, logger: Logger=None, serializer=MyPickleSerializer):
        self.database_file = database_file
        self.read_only = read_only
        self.logger = logger
        self.serializer = serializer()
        self.env = lmdb.open(self.database_file, map_size=10 ** 9, max_dbs=len(self.serializer.name_object), readonly=self.read_only)
        self.object_cache = {}

    def cursor(self):
        return self.con.cursor()

    def clean_cache(self):
        self.object_cache = {}

    def __enter__(self):
        self.con = duckdb.connect(self.database_file, read_only=self.read_only)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.con.close()

    def clear_table(self, klass: T, clean=False):
        name = get_object_name(klass)
        with self.env.begin(write=True) as txn:
            txn.drop(self.env.open_db(name.encode('utf-8')), delete=False)

    def insert_one_object(self, db, object):
        key = (row.id, row.version)
        value =  serializer. serialize_data(row)
        with env.begin(write=True, db=db) as txn:
            txn.put(pickle.dumps(key), value)

    def vacuum(self):
        tmp_file = self.database_file + "_compacted.mdb"
        self.env.copy(path=tmp_file, compact=True)
        self.env.close()
        os.rename(tmp_file, self.database_file)
        self.env = lmdb.open(self.database_file, map_size=10 ** 9, max_dbs=len(self.serializer.name_object), readonly=self.read_only)

    def tables(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            # Try to open each database by index, starting from 0 up to max_dbs
            tables = set([])
            for db_index in range(self.env.info()['num_dbs']):
                try:
                    # Try to get the name of each database
                    table = self.env.open_db(db_index=db_index, readonly=True).encode("utf-8")
                    tables.add(self.get_class_by_name(table))
                except lmdb.Error:
                    # If a database doesn't exist, skip it
                    continue
            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def referencing(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.env:
            tables = set([])
            with self.env.begin(write=False, db=self.env.open_db(b'referencing', readonly=True)) as txn:
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
            with self.env.begin(write=False, db=self.env.open_db(b'embedded', readonly=True)) as txn:
                cursor = txn.cursor()
                for _key, value in cursor:
                    _parent_class, _parent_id, _parent_version, klass, _id, _version, _order, _path = pickle.loads(value)
                    tables.add(self.get_class_by_name(klass))

            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def get_class_by_name(self, name: str):
        return self.serializer.name_object[name]
