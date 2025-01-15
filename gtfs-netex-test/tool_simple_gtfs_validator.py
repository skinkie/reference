import pandas as pd
import zipfile
from aux_logging import *
import traceback
def check_gtfs_consistency(gtfs_file):
    try:
        # Read GTFS files using pandas
        with zipfile.ZipFile(gtfs_file, 'r') as zip_ref:
            df_agency = pd.read_csv(zip_ref.open('agency.txt'))
            df_stops = pd.read_csv(zip_ref.open('stops.txt'))
            df_routes = pd.read_csv(zip_ref.open('routes.txt'))
            df_trips = pd.read_csv(zip_ref.open('trips.txt'))
            df_stop_times = pd.read_csv(zip_ref.open('stop_times.txt'))

        # Perform consistency checks
        errors = []

        # Check if agency_id exists in agency.txt
        if 'agency_id' not in df_agency.columns:
            errors.append("Missing 'agency_id' column in agency.txt")

        # Check if stop_id exists in stops.txt
        if 'stop_id' not in df_stops.columns:
            errors.append("Missing 'stop_id' column in stops.txt")

        # Check if route_id exists in routes.txt
        if 'route_id' not in df_routes.columns:
            errors.append("Missing 'route_id' column in routes.txt")

        # Check if route_id and trip_id exist in trips.txt
        if 'route_id' not in df_trips.columns or 'trip_id' not in df_trips.columns:
            errors.append("Missing 'route_id' or 'trip_id' columns in trips.txt")

        # Check if trip_id, stop_id, and stop_sequence exist in stop_times.txt
        if 'trip_id' not in df_stop_times.columns or 'stop_id' not in df_stop_times.columns or 'stop_sequence' not in df_stop_times.columns:
            errors.append("Missing 'trip_id', 'stop_id', or 'stop_sequence' columns in stop_times.txt")

        # Additional consistency checks can be added based on specific requirements

        if errors:
            log_all(logging.ERROR, "GTFS feed has the following issues:")
            for error in errors:
                log_all(logging.ERROR,error)
            return False
        else:
            log_all(logging.INFO, "GTFS feed is internally consistent.")
            return True

    except Exception as e:
        log_all(logging.ERROR, "Error occurred while checking GTFS consistency:", str(e))
        return False

def check_gtfs_validity(gtfs_file):
    # Read GTFS files using pandas
    invalid=False
    with zipfile.ZipFile(gtfs_file, 'r') as zip_ref:
        try:
            # Check required files
            required_files = {'agency.txt', 'stops.txt','calendar.txt','calendar_dates.txt', 'routes.txt', 'trips.txt', 'stop_times.txt'}
            cond_required_files = {}
            cond_required_files['stops.txt'] = 'locations.geojson'
            cond_required_files['calendar.txt'] = 'calendar_dates.txt'
            cond_required_files['calendar_dates.txt'] = 'calendar.txt'
            gtfs_files = set(zip_ref.namelist())
            missing_files = required_files - gtfs_files
            for missing_file in missing_files:
                if not cond_required_files[missing_file] in gtfs_files:
                    log_all(logging.ERROR,f"Missing required file: {missing_file}")
                    invalid = True
                    return False
            # Check if all required columns are present
            required_columns = {
                'agency.txt': ['agency_id', 'agency_name', 'agency_url'],
                'stops.txt': ['stop_id', 'stop_name', 'stop_lat', 'stop_lon'],
                'routes.txt': ['route_id', 'route_short_name'],
                'trips.txt': ['route_id', 'trip_id'],
                'stop_times.txt': ['trip_id', 'stop_id', 'stop_sequence']
            }
            # 'calendar.txt': ['service_id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
            #                 'start_date', 'end_date'],
            # 'calendar_dates.txt': ['service_id', 'date', 'exception_type'],
            for file, columns in required_columns.items():
                df = pd.read_csv(zip_ref.open(file))
                missing_columns = set(columns) - set(df.columns)
                if missing_columns:
                    log_all(logging.ERROR,f"Missing columns in {file}: {missing_columns}")
                    return False

            # Additional validation checks can be added based on specific requirements

            # If all checks pass, the GTFS file is considered valid
            return True

        except Exception as e:
            log_all(logging.ERROR,f"Error occurred while checking GTFS validity:{str(e)}")
            return False
def get_gtfs_stats(gtfs_file):
    stats = {}

    # Read GTFS files using pandas
    with zipfile.ZipFile(gtfs_file, 'r') as zip_ref:
        try:
            # Get the list of file names in the GTFS ZIP
            gtfs_files = zip_ref.namelist()

            # Count the number of files
            stats['File Count'] = len(gtfs_files)

            # Count the number of records in each file
            for file in gtfs_files:
                df = pd.read_csv(zip_ref.open(file))
                stats[file] = len(df)

            # Additional statistics can be calculated based on specific requirements

        except Exception as e:
            log_all(logging.ERROR,f"Error occurred while processing GTFS file: {str(e)}")

    return stats

def print_stats(stats):
    log_all(logging.INFO,"GTFS Statistics:")
    for key, value in stats.items():
        log_all(logging.INFO,f"{key}: {value}")

def main(gtfs_file):
    if check_gtfs_validity(gtfs_file):
        log_print("The GTFS file is valid.")
    else:
        log_print("The GTFS file is not valid.")
        exit(1)
    if not check_gtfs_consistency(gtfs_file):
        exit(1)
    stats = get_gtfs_stats(gtfs_file)
    print_stats(stats)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Validates a gtfs file and shows some stats')
    parser.add_argument('gtfs_file', type=str, help='The input file (gtfs.zip)')
    parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)

    try:
        main(args.gtfs_file)
    except Exception as e:
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
        raise e
