import duckdb as sqlite3
import os

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

SWISS_CLASSES = ["Codespace", "StopPlace", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "TemplateServiceJourney", "PassengerStopAssignment", "AvailabilityCondition", "TopographicPlace", "ResponsibilitySet"]

def main(swiss_zip_file: str, database: str, clean_database: bool = True):
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

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import a Swiss NeTEx ZIP archive into DuckDB')
    argument_parser.add_argument('swiss_zip_file', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('clean_database', action="store_true", help='Clean the current file', default=True)
    args = argument_parser.parse_args()

    main(args.swiss_zip_file, args.database, args.clean_database)