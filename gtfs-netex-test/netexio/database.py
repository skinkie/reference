from logging import Logger
from typing import T

import duckdb

from netexio.pickleserializer import MyPickleSerializer
from netexio.serializer import Serializer


class Database:
    database_file: str
    read_only: bool
    serializer: Serializer
    con: duckdb.DuckDBPyConnection

    def __init__(self, database_file: str, read_only: bool=True, logger: Logger=None, serializer=MyPickleSerializer):
        self.con = None
        self.database_file = database_file
        self.read_only = read_only
        self.logger = logger
        self.serializer = serializer()

    def cursor(self):
        return self.con.cursor()

    def __enter__(self):
        self.con = duckdb.connect(self.database_file, read_only=self.read_only)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.con.close()

    def tables(self, exclusively: set[T]=None):
        if exclusively is None:
            exclusively = set(self.serializer.interesting_classes)

        if self.con:
            cur = self.con.cursor()
            cur.execute("SELECT table_name FROM information_schema.tables;")
            tables = {self.get_class_by_name(table) for table, in cur.fetchall() if table[0].isupper()} # TODO: Remove other classes from default namespace!
            return sorted(tables.intersection(exclusively), key=lambda v: v.__name__)

    def get_class_by_name(self, name: str):
        return self.serializer.name_object[name]