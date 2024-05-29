import sqlite3

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

DATABASE_FILE = "/home/netex/lux.sqlite"
LUX_ZIP_FILE = "/tmp/netex-20240326-20240531.zip"
CLEAN_DATABASE = True

LUX_CLASSES = [ "Authority", "AvailabilityCondition", "Codespace", "DataSource", "DayType", "DayTypeAssignment", "Direction", "Level", "Line", "Notice", "Operator", "PassengerStopAssignment", "ResponsibilitySet", "ScheduledStopPoint", "ServiceCalendar", "ServiceJourney", "ServiceJourneyInterchange", "ServiceJourneyPattern", "ServiceLink", "SiteConnection",  "StopPlace", "TopographicPlace", "UicOperatingPeriod", "VehicleType" ]

def main():
    with sqlite3.connect(DATABASE_FILE) as con:
        classes = get_interesting_classes(LUX_CLASSES)

        if CLEAN_DATABASE:
            setup_database(con, classes, CLEAN_DATABASE)

        setup_database(con, classes, False)
        for file in open_netex_file(LUX_ZIP_FILE):
            insert_database(con, classes, file)

if __name__ == '__main__':
    main()