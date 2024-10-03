import logging

import duckdb
from aux_logging import *
def print_table_row_counts_with_example(db_file):
    logger=prepare_logger(logging.WARNING,None,"auxh_check_db")
    # Connect to the DuckDB database
    con = duckdb.connect(database=db_file)

    # Get the list of tables in the database
    tables = con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    # Iterate over each table and retrieve the row count
    for table in tables:
        table_name = table[0]
        row_count = con.execute(f"SELECT COUNT(*) FROM {table_name};").fetchone()[0]
        logger.log(logging.INFO,f"{table_name}: {row_count}")

        # Select a random row from the table
        random_row = con.execute(f"SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT 1;").fetchone()
        if random_row:
            # Convert the row to a string
            row_string = " | ".join(str(col) for col in random_row)
            log_print(f"{table_name}_example: {row_string}")
        else:
            log_print(f"{table_name}_example: No rows found in the table")

    # Close the database connection
    con.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Check the content of a duckdb')
    parser.add_argument('db_file', type=str, help='tthe duckdb-file')
    args = parser.parse_args()

    print_table_row_counts_with_example(args.db_file)