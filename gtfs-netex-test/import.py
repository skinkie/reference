import duckdb

con = duckdb.connect(database='gtfs2.duckdb')
with duckdb.cursor(con) as cur:
    cur.execute("""CREATE TABLE feed_info AS SELECT * FROM read_csv('gtfs/feed_info.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE agency AS SELECT * FROM read_csv('gtfs/agency.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE calendar_dates AS SELECT * FROM read_csv('gtfs/calendar_dates.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE calendar AS SELECT * FROM read_csv('gtfs/calendar.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE routes AS SELECT * FROM read_csv('gtfs/routes.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE stops AS SELECT * FROM read_csv('gtfs/stops.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE shapes AS SELECT * FROM read_csv('gtfs/shapes.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE trips AS SELECT * FROM read_csv('gtfs/trips.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE transfers AS SELECT * FROM read_csv('gtfs/transfers.txt', delim=',', header=true, auto_detect=true);""")
    cur.execute("""CREATE TABLE stop_times AS SELECT * FROM read_csv('gtfs/stop_times.txt', delim=',', header=true, auto_detect=true);""")\

con.close()