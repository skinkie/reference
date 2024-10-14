import sys

import duckdb as sqlite3
import os
import xml.etree.ElementTree as ET

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database
from aux_logging import *
import traceback
from netexio.dbaccess import resolve_all_references

SWISS_CLASSES = ["Codespace", "StopPlace", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "TemplateServiceJourney", "ServiceCalendar", "PassengerStopAssignment", "AvailabilityCondition", "TopographicPlace", "ResponsibilitySet"]

def main(swiss_zip_file: str, database: str, clean_database: bool = True, referencing: bool = False):
    for file in open_netex_file(swiss_zip_file):
        if file.name.endswith(".xml"):
            if not check_if_swiss_file(file):
                # TODO: Wouldn't it be more efficient to check the filename structure?
                print("Not enough elements with id attributes starting with ch:1:. So no Swiss data")
                sys.exit(2)

    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    try:
        os.remove(database)
    except:
        pass

    with sqlite3.connect(database) as con:
        classes = get_interesting_classes(SWISS_CLASSES)

        setup_database(con, classes, clean_database)

        for file in open_netex_file(swiss_zip_file):
            insert_database(con, classes, file)

        if referencing:
            resolve_all_references(con, classes)

def check_if_swiss_file(file_handler):
    if file_handler.name.endswith(".xml"):
        tree = ET.parse(file_handler)
        root = tree.getroot()
        count = 0
        for elem in root.iter():
            if "id" in elem.attrib and elem.attrib["id"].startswith("ch:1:"):
                count += 1
                if count > 10:
                    return True
        return False


if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import a Swiss NeTEx ZIP archive into DuckDB')
    argument_parser.add_argument('swiss_zip_file', type=str, help='The NeTEx zip file')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('--clean_database', action="store_true", help='Clean the current file', default=True)
    argument_parser.add_argument('--referencing', action="store_false", help='Create referencing table')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)
    try:
        main(args.swiss_zip_file, args.database, args.clean_database,args.referencing)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())