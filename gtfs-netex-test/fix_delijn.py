import duckdb
import hashlib
import struct
import sys


def get_unique_value(id_str, max_digits):
    try:
        # Create SHA-1 hash object
        sha = hashlib.sha1()

        # Update hash object with bytes of the input string
        sha.update(id_str.encode('utf-8'))

        # Get the digest (hash result)
        result = sha.digest()

        return result.hex()[0:max_digits]

        # Unpack the first 8 bytes of the result as a long integer
        # long_val = struct.unpack('>Q', result[:8])[0]

        # Take absolute value and apply modulo to get desired number of digits
        # return abs(long_val) % (10 ** max_digits)

    except Exception as e:
        raise
        # In case of any error, return the minimum value for a 64-bit integer
        return -9223372036854775808  # This is equivalent to Long.MIN_VALUE in Java


# Connect to a database (or create one if it doesn't exist)
con = duckdb.connect(sys.argv[1])

# Register the function with DuckDB
# con.create_function("get_unique_value", get_unique_value, ['VARCHAR', 'INTEGER'], 'VARCHAR')

# Use the function in a SQL query
# result = con.execute("""UPDATE stop_times SET trip_id = get_unique_value(trips.trip_id, 20) FROM trips WHERE trips.trip_id = stop_times.trip_id; """).fetchall()
# result = con.execute("""UPDATE trips SET trip_id = get_unique_value(trip_id, 8);""").fetchall()

result = con.execute("""UPDATE stop_times SET trip_id = substring(md5(trip_id), 0, 10);""").fetchall()
result = con.execute("""UPDATE trips SET trip_id = substring(md5(trip_id), 0, 10);""").fetchall()
