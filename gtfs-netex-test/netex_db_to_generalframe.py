from typing import List

from netexio.database import Database
from netexio.dbaccess import get_interesting_classes, setup_database, open_netex_file, insert_database
from aux_logging import *
from netexio.generalframe import export_to_general_frame
from transformers.embedding import embedding_update


def main(database: str, output_filename: str):
    with Database(database, read_only=True) as db_read:
        export_to_general_frame(db_read, output_filename)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import any NeTEx source into DuckDB')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('output_filename', type=str, help='The output filename DuckDB')
    args = argument_parser.parse_args()

    main(args.database, args.output_filename)