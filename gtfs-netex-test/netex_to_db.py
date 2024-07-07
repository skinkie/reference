from typing import List

import duckdb as sqlite3
import os

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

def main(filenames: List[str], database: str, clean_database: bool = True):
    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    try:
        os.remove(database)
    except:
        pass

    with sqlite3.connect(database) as con:
        classes = get_interesting_classes()

        if clean_database:
            setup_database(con, classes, clean_database)

        for filename in filenames:
            for sub_file in open_netex_file(filename):
                insert_database(con, classes, sub_file)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import any NeTEx source into DuckDB')
    argument_parser.add_argument('netex', nargs='+', default=[], help='NeTEx files')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('clean_database', action="store_true", help='Clean the current file', default=True)
    args = argument_parser.parse_args()

    main(args.netex, args.database, args.clean_database)