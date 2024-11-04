from netex import ScheduledStopPoint
from netexio.dbaccess import load_local
import duckdb
import time
con = duckdb.connect('/tmp/keolis.duckdb')

now = time.time()
ssps = load_local(con, ScheduledStopPoint)
print(len(ssps))
print(time.time() - now)