import duckdb
from chardet.universaldetector import UniversalDetector
from os.path import exists
FOLDER="gtfs/"

def detectencoding(filename):
    detector = UniversalDetector()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result

files= ["feed_info","agency","calendar_dates","routes","stops","shapes","trips","transfers","stop_times"]

con = duckdb.connect(database='gtfs2.duckdb')
with duckdb.cursor(con) as cur:
    for file in files:

        dtstring="""DROP TABLE IF EXISTS """+ file;
        cur.execute(dtstring)
        if exists(FOLDER+file+".txt"):
            encoding=detectencoding(FOLDER+file+".txt")
            if (encoding["encoding"]!="utf-8" and encoding["encoding"]!="UTF-8-SIG"):
                print ("encoding faulty for duckdb.read_csv. Can only safely process UTF-8: "+file)
            crstring="CREATE TABLE "+file+" AS SELECT * FROM read_csv('"+FOLDER+file+".txt', delim=',', header=true, auto_detect=true, normalize_names=true, ignore_errors=true)"
            #normalize_names should ignore the BOM in the header
            #ignore_errors generates an error table for later processing
            cur.execute(crstring)
        else:
            print("file missing: "+file)
