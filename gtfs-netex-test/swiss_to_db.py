import sqlite3

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

DATABASE_FILE = "/home/netex/swiss.sqlite"
SWISS_ZIP_FILE = "/home/skinkie/Downloads/prod_netex_tt_1.10_che_ski_2024_oev-schweiz__1_1_202404140804.zip"
CLEAN_DATABASE = False

SWISS_CLASSES = ["Codespace", "StopPlace", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "PassengerStopAssignment", "AvailabilityCondition", "TopographicPlace"]
def main():
    with sqlite3.connect(DATABASE_FILE) as con:
        classes = get_interesting_classes(SWISS_CLASSES)

        if CLEAN_DATABASE:
            setup_database(con, classes, CLEAN_DATABASE)

        setup_database(con, classes, False)
        for file in open_netex_file(SWISS_ZIP_FILE):
            insert_database(con, classes, file)

if __name__ == '__main__':
    main()