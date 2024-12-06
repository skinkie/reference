import csv
from aux_logging import *
import traceback
import zipfile
import io

def get_data_gtfs(zip_file_path, origin_stop_id,origin_dep_time):
    trips  = {}
    origins = {}
    origin_stop_times = {}
    with zipfile.ZipFile(zip_file_path, 'r') as gtfs_zip:
        # find the stop_times for each route that start
        file_name="stop_times.txt"
        if file_name in gtfs_zip.namelist():
            with gtfs_zip.open(file_name, 'r') as file:
                file = io.TextIOWrapper(file, encoding='utf-8')  # Open the file in text mode
                reader = csv.DictReader(file)
                inparse=False
                for row in reader:
                    id = row["trip_id"]
                    if row['stop_sequence']=="1":
                        if row['departure_time']==origin_dep_time and row['stop_id']==origin_stop_id:
                            origins[id] = row
                            inparse=True
                            parsetripid=id
                            origin_stop_times = {}
                    if inparse:
                        if row['trip_id']==parsetripid:
                            origin_stop_times[row['stop_sequence']]=row
                        else:
                            inparse=False
                            origins[parsetripid]['origin_stop_times']=origin_stop_times

            print(f"File '{file_name}' read successfully.")
        else:
            print(f"File '{file_name}' not found in the GTFS zip.")

        if len(origins)>1:
            print(f'Too many origins')
        elif len(origins)==0:
            print(f'not found')
        # print the result
        for origin_key in origins:
            origin=origins[origin_key]
            for key,row in origin['origin_stop_times'].items():

                print (f"{row['stop_sequence']:3s} - {row['stop_id']:40s} - {row['arrival_time']:12s} - {row['departure_time']:12s}")
    return


if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Extract the stop sequence for a single stop')
    argument_parser.add_argument('zip_file_path', type=str, help='GTFS file path')
    argument_parser.add_argument('origin_stop_id', type=str, help='Origin of the trip')
    argument_parser.add_argument('origin_dep_time',  type=str, help='Departure time of the trip')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)
    try:
        get_data_gtfs(args.zip_file_path, args.origin_stop_id, args.origin_dep_time)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e