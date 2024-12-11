from typing import List

from netexio.database import Database
from netexio.dbaccess import get_interesting_classes, setup_database, open_netex_file, insert_database
from aux_logging import *
from transformers.embedding import embedding_update


def main(filenames: List[str], database: str, clean_database: bool = True, referencing: bool = False):

    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    if clean_database:
        try:
            os.remove(database)
        except:
            pass

    with Database(database, read_only=False, logger=logging.getLogger("script_runner")) as db:
        classes = get_interesting_classes()

        if clean_database:
            setup_database(db, classes, clean_database)

        for filename in filenames:
            for sub_file in open_netex_file(filename):
                insert_database(db, classes, sub_file)

        embedding_update(db)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import any NeTEx source into DuckDB')
    argument_parser.add_argument('netex', nargs='+', default=[], help='NeTEx files')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('--clean_database', action="store_true", help='Clean the current file', default=True)
    args = argument_parser.parse_args()

    main(args.netex, args.database, args.clean_database)