import duckdb
import time

def run_query1(con):
  cur = con.cursor()
  cur.execute("SELECT object FROM test;")
  cur.fetchall()


def run_query2(con):
  cur = con
  cur.execute("SELECT object FROM test;")
  cur.fetchall()


with duckdb.connect(":memory:") as con:
  con.execute("DROP TABLE IF EXISTS test;")
  con.execute("CREATE TABLE test (object TEXT);")
  for i in range(0, 10000):
    con.execute("INSERT INTO test VALUES ('Hello world');")

  now = time.time()
  for i in range(0, 1000):
    run_query1(con)

  _now = now
  now = time.time()
  print(now - _now)

with duckdb.connect(":memory:") as con:
  con.execute("DROP TABLE IF EXISTS test;")
  con.execute("CREATE TABLE test (object TEXT);")
  for i in range(0, 10000):
    con.execute("INSERT INTO test VALUES ('Hello world');")

  now = time.time()
  for i in range(0, 1000):
    run_query2(con)

  _now = now
  now = time.time()
  print(now - _now)