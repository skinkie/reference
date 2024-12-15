import os
from typing import List

from netexio.database import Database
from netexio.dbaccess import setup_database, open_netex_file, insert_database, \
    resolve_all_references_and_embeddings
from utils import get_interesting_classes
from transformers.embedding import embedding_update

DUTCH_CLASSES = ["Authority", "AvailabilityCondition", "Block", "Branding", "DataSource", "DayType", "DayTypeAssignment", "DeadRun", "DeadRunJourneyPattern", "DestinationDisplay", "Line", "Notice", "NoticeAssignment", "OperationalContext", "Operator", "PassengerStopAssignment", "ResponsibilitySet", "Route", "RouteLink", "RoutePoint", "ScheduledStopPoint", "ServiceJourney", "ServiceJourneyPattern", "StopArea", "TimeDemandType", "TimingLink", "TimingPoint", "TransportAdministrativeZone", "TypeOfProductCategory", "VehicleType", "Version"]

DUTCH_TYPE_OF_FRAME = {'BISON:TypeOfFrame:NL_TT_BASELINE', 'BISON:TypeOfFrame:NL_TT_DELTA', 'BISON:TypeOfFrame:NL_CODESPACES', 'BISON:TypeOfFrame:NL_BISON_ENUMS', 'BISON:TypeOfFrame:NL_DOVA_LISTS', 'BISON:TypeOfFrame:NL_VEHICLES', 'BISON:TypeOfFrame:NL_TT_RESOURCE', 'BISON:TypeOfFrame:NL_TT_INFRA', 'BISON:TypeOfFrame:NL_TT_SERVICE', 'BISON:TypeOfFrame:NL_TT_TIMETABLE', 'BISON:TypeOfFrame:NL_TT_CALENDAR', 'BISON:TypeOfFrame:NL_TT_VEHICLE', 'BISON:TypeOfFrame:NL_TT_SITE', 'BISON:TypeOfFrame:NL_AuthorityList', 'BISON:TypeOfFrame:NL_TariffZoneList', 'BISON:TypeOfFrame:NL_NetworkList', 'BISON:TypeOfFrame:NL_TypeOfEquipmentValues', 'BISON:TypeOfFrame:NL_TypeOfActivationValues', 'BISON:TypeOfFrame:NL_TypeOfServiceValues', 'BISON:TypeOfFrame:NL_TechnicalEnumerations', 'BISON:TypeOfFrame:NL_VEH_METADATA', 'BISON:TypeOfFrame:NL_VEH_DATA'}

def main(filenames: List[str], database: str, clean_database: bool = True, referencing: bool = False):
    if clean_database:
        # Workaround for https://github.com/duckdb/duckdb/issues/8261
        try:
            os.remove(database)
        except:
            pass

    with Database(database) as db:
        classes = get_interesting_classes()

        if clean_database:
            setup_database(db, classes, clean_database)

        for filename in filenames:
            for sub_file in open_netex_file(filename):
                insert_database(db, classes, sub_file, DUTCH_TYPE_OF_FRAME)

        if referencing:
            embedding_update(db)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Import a Dutch NeTEx XML into DuckDB')
    argument_parser.add_argument('netex', nargs='+', default=[], help='NeTEx files')
    argument_parser.add_argument('database', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    argument_parser.add_argument('--clean_database', action="store_true", help='Clean the current file', default=True)
    argument_parser.add_argument('--referencing', action="store_true", help='Create referencing table')
    args = argument_parser.parse_args()

    main(args.netex, args.database, args.clean_database, args.referencing)