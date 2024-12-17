import duckdb

ro_file = 'ro.duckdb'
rw_file = 'rw.duckdb'

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

def copy_table(db_read: Database, db_write: Database, classes: list, clean=False):
    sql = f"ATTACH DATABASE '{db_read.database_file}' AS db_read (READ_ONLY);"
    print(sql)
    db_write.con.execute(sql)
    db_write.con.execute(f"DETACH db_read;")

"""
with Database(rw_file, read_only=False) as target_db:
    with Database(ro_file, read_only=True) as source_db:
        copy_table(source_db, target_db, ['test'])
"""

with duckdb.connect(rw_file, read_only=False) as target_db:
    cur_rw = target_db.cursor()

    with duckdb.connect(ro_file, read_only=True) as source_db:
        cur_ro = source_db.cursor()

        cur_rw.execute(f"ATTACH DATABASE '{ro_file}' AS db_read (READ_ONLY);")
        cur_rw.execute(f"DETACH db_read;")

        print(cur_ro)
