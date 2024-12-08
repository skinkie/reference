import os

from netexio.database import Database
from netexio.dbaccess import get_interesting_classes, setup_database, open_netex_file, insert_database

DATABASE_FILE = "/home/netex/lux.sqlite"
LUX_ZIP_FILE = "/home/skinkie/Downloads/netex-20240916-20240705.zip"
CLEAN_DATABASE = True

LUX_CLASSES = [ "Authority", "AvailabilityCondition", "Codespace", "DataSource", "DayType", "DayTypeAssignment", "Direction", "Level", "Line", "Notice", "Operator", "PassengerStopAssignment", "ResponsibilitySet", "ScheduledStopPoint", "ServiceCalendar", "ServiceJourney", "ServiceJourneyInterchange", "ServiceJourneyPattern", "ServiceLink", "SiteConnection",  "StopPlace", "TopographicPlace", "UicOperatingPeriod", "VehicleType" ]

def main():
    with Database(DATABASE_FILE) as db:
        classes = get_interesting_classes(LUX_CLASSES)

        if CLEAN_DATABASE:
            try:
                os.remove(DATABASE_FILE)
            except:
                pass

        setup_database(db, classes, CLEAN_DATABASE)
        for file in open_netex_file(LUX_ZIP_FILE):
            insert_database(db, classes, file)

if __name__ == '__main__':
    main()