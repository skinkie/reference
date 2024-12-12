from logging import Logger

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
        self.con = duckdb.connect(self.database_file)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.con.close()

    def tables(self, exclusively: set[str]=None):
        if exclusively is None:
            exclusively = set(self.serializer.clean_element_names)

        if self.con:
            cur = self.con.cursor()
            cur.execute("SELECT table_name FROM information_schema.tables;")
            tables = {table for table, in cur.fetchall()}
            return tables.intersection(exclusively)
