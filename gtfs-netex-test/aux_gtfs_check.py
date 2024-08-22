import pandas as pd
import zipfile

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
            print("GTFS feed has the following issues:")
            for error in errors:
                print(error)
            return False
        else:
            print("GTFS feed is internally consistent.")
            return True

    except Exception as e:
        print("Error occurred while checking GTFS consistency:", str(e))
        return False

def check_gtfs_validity(gtfs_file):
    # Read GTFS files using pandas
    with zipfile.ZipFile(gtfs_file, 'r') as zip_ref:
        try:
            # Check required files
            required_files = {'agency.txt', 'stops.txt', 'routes.txt', 'trips.txt', 'stop_times.txt'}
            gtfs_files = set(zip_ref.namelist())
            missing_files = required_files - gtfs_files
            if missing_files:
                print("Missing required files:", missing_files)
                return False

            # Check if all required columns are present
            required_columns = {
                'agency.txt': ['agency_id', 'agency_name', 'agency_url'],
                'stops.txt': ['stop_id', 'stop_name', 'stop_lat', 'stop_lon'],
                'routes.txt': ['route_id', 'route_short_name'],
                'trips.txt': ['route_id', 'trip_id'],
                'stop_times.txt': ['trip_id', 'stop_id', 'stop_sequence']
            }
            for file, columns in required_columns.items():
                df = pd.read_csv(zip_ref.open(file))
                missing_columns = set(columns) - set(df.columns)
                if missing_columns:
                    print("Missing columns in", file, ":", missing_columns)
                    return False

            # Additional validation checks can be added based on specific requirements

            # If all checks pass, the GTFS file is considered valid
            return True

        except Exception as e:
            print("Error occurred while checking GTFS validity:", str(e))
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
            print("Error occurred while processing GTFS file:", str(e))

    return stats

def print_stats(stats):
    print("GTFS Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

def main(gtfs_file):
    if check_gtfs_validity(gtfs_file):
        print("The GTFS file is valid.")
    else:
        print("The GTFS file is not valid.")
        exit(1)
    if not check_gtfs_consistency(gtfs_file):
        exit(1)
    stats = get_gtfs_stats(gtfs_file)
    print_stats(stats)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Validates a gtfs file and shows some stats')
    parser.add_argument('gtfs_file', type=str, help='The input file (gtfs.zip)')
    args = parser.parse_args()

    main(args.gtfs_file)