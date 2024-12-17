import duckdb

ro_file = 'ro.duckdb'
rw_file = 'rw.duckdb'

duckdb.connect(ro_file, read_only=False)

class Database:
    database_file: str
    read_only: bool
    con: duckdb.DuckDBPyConnection

    def __init__(self, database_file: str, read_only: bool=True):
        self.con = None
        self.database_file = database_file
        self.read_only = read_only

    def cursor(self):
        return self.con.cursor()

    def __enter__(self):
        self.con = duckdb.connect(self.database_file)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.con.close()


"""
with duckdb.connect(rw_file, read_only=False) as target_db:
    with duckdb.connect(ro_file, read_only=True) as source_db:
        target_db.execute(f"ATTACH DATABASE '{ro_file}' AS db_read (READ_ONLY);")
        target_db.execute(f"DETACH db_read;")

        print(source_db)
"""

with Database(rw_file, read_only=False) as target_db:
    with Database(ro_file, read_only=True) as source_db:
        target_db.con.execute(f"ATTACH DATABASE '{ro_file}' AS db_read (READ_ONLY);")   
        target_db.con.execute(f"DETACH db_read;")