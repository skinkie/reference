from typing import List

import duckdb as sqlite3
import os

from netexio.dbaccess import get_interesting_classes, setup_database, open_netex_file, insert_database, \
    resolve_all_references_and_embeddings
from aux_logging import *


def main(filenames: List[str], database: str, clean_database: bool = True, referencing: bool = False):
    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    if clean_database:
        try:
            os.remove(database)
        except:
            pass

    with sqlite3.connect(database) as con:
        classes = get_interesting_classes()

        setup_database(con, classes, clean_database)

        for filename in filenames:
            for sub_file in open_netex_file(filename):
                insert_database(con, classes, sub_file)

        if referencing:
            resolve_all_references_and_embeddings(con, classes)

if __name__ == '__main__':
    import argparse
    global mylogger
    argument_parser = argparse.ArgumentParser(description='Import any NeTEx source into DuckDB')
    argument_parser.add_argument('netex', nargs='+', default=[], help='NeTEx files')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('clean_database', action="store_true", help='Clean the current file', default=True)
    argument_parser.add_argument('clean_database', action="store_true", help='Clean the current file')
    argument_parser.add_argument('referencing', action="store_false", help='Create referencing table')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)


    # main(args.netex, args.database, args.clean_database, args.referencing)
    main(args.netex, args.database, False, args.referencing)
