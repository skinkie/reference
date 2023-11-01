# Import files in DuckDB

CREATE TABLE agency AS SELECT * FROM read_csv('/tmp/eu/agency.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE calendar_dates AS SELECT * FROM read_csv('/tmp/eu/calendar_dates.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE calendar AS SELECT * FROM read_csv('/tmp/eu/calendar.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE routes AS SELECT * FROM read_csv('/tmp/eu/routes.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE stops AS SELECT * FROM read_csv('/tmp/eu/stops.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE shapes AS SELECT * FROM read_csv('/tmp/eu/shapes.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE trips AS SELECT * FROM read_csv('/tmp/eu/trips.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE transfers AS SELECT * FROM read_csv('/tmp/eu/transfers.txt', delim=',', header=true, auto_detect=true);
CREATE TABLE stop_times AS SELECT * FROM read_csv('/tmp/eu/stop_times.txt', delim=',', header=true, auto_detect=true);
