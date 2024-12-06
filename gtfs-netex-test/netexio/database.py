import duckdb

from netexio.pickleserializer import MyPickleSerializer
from netexio.serializer import Serializer


class Database:
    database_file: str
    read_only: bool
    serializer: Serializer
    con: duckdb.DuckDBPyConnection

    def __init__(self, database_file: str, read_only=True, serializer=MyPickleSerializer):
        self.database_file = database_file
        self.read_only = read_only
        self.serializer = serializer()

    def cursor(self):
        return self.con.cursor()

    def __enter__(self):
        self.con = duckdb.connect(self.database_file)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.con.close()