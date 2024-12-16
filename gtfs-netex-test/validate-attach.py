import duckdb

from netex import TariffZone

with duckdb.connect("/tmp/ro.duckdb", read_only=False) as ro:
    ro.execute("CREATE TABLE test AS SELECT 1 AS test;")

with duckdb.connect("/tmp/rw.duckdb") as rw:
    with duckdb.connect("/tmp/ro.duckdb", read_only=True) as ro:
        rw.execute("ATTACH IF NOT EXISTS '/tmp/ro.duckdb' AS db_read (READ_ONLY);")
        rw.execute("CREATE TABLE test2 AS SELECT * FROM db_read.test;")

TariffZone(type)