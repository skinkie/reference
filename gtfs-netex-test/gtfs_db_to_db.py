import logging
import traceback
import os

from aux_logging import prepare_logger, log_all
from netex import DataSource, Codespace, StopPlace, PassengerStopAssignment, ScheduledStopPoint, AvailabilityCondition, \
    DayType, DayTypeAssignment, UicOperatingPeriod
from netexio.database import Database
from netexio.dbaccess import setup_database,  write_objects, load_local, copy_table
from utils import get_interesting_classes
from transformers.gtfs import GTFS_CLASSES, gtfs_operator_line_memory, gtfs_calls_generator, \
    apply_availability_conditions_via_day_type_ref
from transformers.projection import reprojection_update


def main(source_database_file: str, target_database_file: str, clean_database: bool=True):
    classes = get_interesting_classes(GTFS_CLASSES)

    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    if clean_database:
        try:
            os.remove(target_database_file)
        except:
            pass


    with Database(target_database_file, read_only=False) as db_write:
        setup_database(db_write, classes, True)

        with Database(source_database_file, read_only=True) as db_read:
            # Copy tables that we don't change as-is.
            copy_table(db_read, db_write,[DataSource, Codespace, StopPlace, PassengerStopAssignment, ScheduledStopPoint], clean=True)

            # Flatten the Operator, Authority, Branding, ResponsibilitySet
            gtfs_operator_line_memory(db_read, db_write, {})

            apply_availability_conditions_via_day_type_ref(db_read, db_write)

            # rewrite to override the db_write
            # gtfs_calls_generator(db_read, db_write, {})

            # Extract calendar information
            # gtfs_calendar_generator(db_read, db_write, {})

        # Our target database must be reprojected to WGS84            apply_availability_conditions_via_day_type_ref(db_read, db_write)

        reprojection_update(db_write, crs_to="urn:ogc:def:crs:EPSG::4326")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Transform the input into mandatory objects for the export of GTFS')
    parser.add_argument('source', type=str, help='DuckDB file to use as input of the transformation.')
    parser.add_argument('target', type=str, help='DuckDB file to overwrite and store contents of the transformation.')
    parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)
    try:
        main(args.source, args.target)
    except Exception as e:
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
        raise e
