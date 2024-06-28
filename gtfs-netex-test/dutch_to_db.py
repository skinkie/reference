import duckdb as sqlite3

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

DATABASE_FILE = "/home/netex/dutch.duckdb"
NETEX_FILENAME = "/home/skinkie/Downloads/prod_netex_tt_1.10_che_ski_2024_oev-schweiz__1_1_202404140804.zip"
CLEAN_DATABASE = False

DUTCH_CLASSES = ["Authority", "AvailabilityCondition", "Block", "Branding", "DataSource", "DayType", "DayTypeAssignment", "DeadRun", "DeadRunJourneyPattern", "DestinationDisplay", "Line", "Notice", "NoticeAssignment", "OperationalContext", "Operator", "PassengerStopAssignment", "ResponsibilitySet", "Route", "RouteLink", "RoutePoint", "ScheduledStopPoint", "ServiceJourney", "ServiceJourneyPattern", "StopArea", "TimeDemandType", "TimingLink", "TimingPoint", "TransportAdministrativeZone", "TypeOfProductCategory", "VehicleType", "Version"]

def main():
    with sqlite3.connect(DATABASE_FILE) as con:
        classes = get_interesting_classes(DUTCH_CLASSES)

        if CLEAN_DATABASE:
            setup_database(con, classes, CLEAN_DATABASE)

        setup_database(con, classes, False)
        for file in open_netex_file(NETEX_FILENAME):
            insert_database(con, classes, file)

if __name__ == '__main__':
    main()