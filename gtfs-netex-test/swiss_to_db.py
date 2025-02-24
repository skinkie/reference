import logging
import sys

import os

from netexio.database import Database
from netexio.dbaccess import resolve_all_references_and_embeddings, open_netex_file, setup_database, insert_database
from utils import get_interesting_classes
from netexio.pickleserializer import MyPickleSerializer
import netex_monkeypatching
from aux_logging import *
import traceback

from transformers.embedding import embedding_update

SWISS_CLASSES = ["Codespace", "StopPlace", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "TemplateServiceJourney", "ServiceCalendar", "PassengerStopAssignment", "AvailabilityCondition", "TopographicPlace", "ResponsibilitySet"]

def main(swiss_zip_file: str, database: str, clean_database: bool = True, referencing: bool = True):
    for file in open_netex_file(swiss_zip_file):
        if file.name.endswith(".xml"):
            if not check_if_swiss_file(file):
                print("File names do not fit Swiss data:. So no Swiss data")
                sys.exit(2)

    with Database(database, MyPickleSerializer(compression=True), read_only=False, logger=logging.getLogger("script_runner")) as db:
        classes = get_interesting_classes(SWISS_CLASSES)

        setup_database(db, classes, clean_database)

        log_all(logging.INFO, f"Starting to load {swiss_zip_file}")
        for file in open_netex_file(swiss_zip_file):
            log_all(logging.INFO, f"Inserting {file.name}")
            insert_database(db, classes, file)

        if referencing:
            log_all(logging.INFO, f"Embedding update!")
            embedding_update(db)

def check_if_swiss_file(file_handler):
    if file_handler.name.endswith(".xml"):
        fn=file_handler.name
        if "_CHE_" not in fn:
            return False
    return True

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import a Swiss NeTEx ZIP archive into DuckDB')
    argument_parser.add_argument('swiss_zip_file', type=str, help='The NeTEx zip file')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('--clean_database', action="store_true", help='Clean the current file', default=True)
    argument_parser.add_argument('--referencing', action="store_true", help='Create referencing table')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)
    try:
        main(args.swiss_zip_file, args.database, args.clean_database,args.referencing)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e
