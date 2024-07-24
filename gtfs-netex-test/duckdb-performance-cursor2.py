from typing import List

import duckdb

def load_generator(con, type, limit=None, filter=None):
  cur = con.cursor()
  try:
    if filter is not None:
      cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
    elif limit is not None:
      cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
      cur.execute(f"SELECT object FROM {type};")
  except:
    return

  while True:
    xml = cur.fetchone()
    if xml is None:
      break
    yield xml[0]

def load_local(con, type, limit=None, filter=None) -> List:
  # cur = con.cursor()
  cur = con
  try:
    if filter is not None:
      cur.execute(f"SELECT object FROM {type} WHERE id = ?;", (filter,))
    elif limit is not None:
      cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
      cur.execute(f"SELECT object FROM {type};")
  except:
    return []

  objs: List = []
  for xml, in cur.fetchall():
    obj = xml
    objs.append(obj)

  return objs

def write_objects(con, objs, objectname):
  if len(objs) == 0:
    return

  # cur = con.cursor()
  cur = con

  for i in range(0, len(objs)):
    obj = objs[i]
    cur.execute(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);',
                (obj[0], obj[1], obj[2].replace('\n', '')))

import timeit

def gen_with_write():
  with duckdb.connect(":memory:") as con:
    con.execute("DROP TABLE IF EXISTS test;")
    con.execute("CREATE TABLE test (id VARCHAR, version VARCHAR, object VARCHAR NOT NULL, PRIMARY KEY(id, version));")

    con.execute("DROP TABLE IF EXISTS test2;")
    con.execute("CREATE TABLE test2 (id VARCHAR, version VARCHAR, object VARCHAR NOT NULL, PRIMARY KEY(id, version));")

    for i in range(0, 10000):
      con.execute("INSERT INTO test VALUES (?, 1, ?);", (str(i), str(i)))

    for x in load_generator(con, "test", limit=10000):
      results = load_local(con, "test2",1, x)
      if len(results) == 0:
        # Notice, this is required to trigger it the write, after load
        write_objects(con, [[x, '1', 'test']], "test2")

def gen_cache_write():
  with duckdb.connect(":memory:") as con:
    con.execute("DROP TABLE IF EXISTS test;")
    con.execute("CREATE TABLE test (id VARCHAR, version VARCHAR, object VARCHAR NOT NULL, PRIMARY KEY(id, version));")

    con.execute("DROP TABLE IF EXISTS test2;")
    con.execute("CREATE TABLE test2 (id VARCHAR, version VARCHAR, object VARCHAR NOT NULL, PRIMARY KEY(id, version));")

    for i in range(0, 10000):
      con.execute("INSERT INTO test VALUES (?, 1, ?);", (str(i), str(i)))

    cache = []

    for x in load_generator(con, "test", limit=10000):
      results = load_local(con, "test2", 1, x)
      if len(results) == 0:
        cache.append([x, '1', 'test'])
        # Notice, this is required to trigger it the write, after load

    write_objects(con, cache, "test2")

print(timeit.timeit("gen_with_write()",  setup="from __main__ import gen_with_write", number=1))
print(timeit.timeit("gen_cache_write()", setup="from __main__ import gen_cache_write", number=1))