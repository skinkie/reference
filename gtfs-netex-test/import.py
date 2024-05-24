import duckdb
import csv
from configuration import BASEDIR, DUCKDB


agency_txt = {'agency_id': 'VARCHAR', 'agency_name': 'VARCHAR', 'agency_url': 'VARCHAR', 'agency_timezone': 'VARCHAR', 'agency_lang': 'VARCHAR', 'agency_phone': 'VARCHAR', 'agency_fare_url': 'VARCHAR', 'agency_email': 'VARCHAR'}
stops_txt = {'stop_id': 'VARCHAR', 'stop_code': 'VARCHAR', 'stop_name': 'VARCHAR', 'tts_stop_name': 'VARCHAR', 'stop_desc': 'VARCHAR', 'stop_lat': 'FLOAT', 'stop_lon': 'FLOAT', 'zone_id': 'VARCHAR', 'stop_url': 'VARCHAR', 'location_type': 'INTEGER', 'parent_station': 'VARCHAR', 'stop_timezone': 'VARCHAR', 'wheelchair_boarding': 'INTEGER', 'level_id': 'VARCHAR', 'platform_code': 'VARCHAR'}
routes_txt = {'route_id': 'VARCHAR', 'agency_id': 'VARCHAR', 'route_long_name': 'VARCHAR', 'route_type': 'INTEGER', 'route_url': 'VARCHAR', 'route_color': 'CHAR(6)', 'route_text_color': 'CHAR(6)', 'route_sort_order': 'INTEGER', 'continuous_pickup': 'INTEGER',  'continuous_drop_off': 'INTEGER', 'network_id': 'VARCHAR'}
trips_txt = {'route_id': 'VARCHAR', 'service_id': 'VARCHAR', 'trip_id': 'VARCHAR', 'trip_headsign': 'VARCHAR', 'trip_short_name': 'VARCHAR', 'direction_id': 'INTEGER', 'block_id': 'VARCHAR', 'shape_id': 'VARCHAR', 'wheelchair_accessible': 'INTEGER', 'bikes_allowed': 'INTEGER'}
stop_times_txt = {'trip_id': 'VARCHAR', 'arrival_time': 'VARCHAR', 'departure_time': 'VARCHAR', 'stop_id': 'VARCHAR', 'location_group_id': 'VARCHAR',  'location_id': 'VARCHAR',  'stop_sequence': 'INTEGER',  'stop_headsign': 'VARCHAR', 'start_pickup_drop_off_window': 'VARCHAR', 'end_pickup_drop_off_window': 'VARCHAR', 'pickup_type': 'INTEGER', 'drop_off_type': 'INTEGER', 'continuous_pickup': 'INTEGER', 'continuous_drop_off': 'INTEGER', 'shape_dist_traveled': 'FLOAT', 'timepoint': 'INTEGER', 'drop_off_booking_rule_id': 'VARCHAR'}
calendar_txt = {'service_id': 'VARCHAR', 'monday': 'INTEGER', 'tuesday': 'INTEGER', 'wednesday': 'INTEGER', 'thursday': 'INTEGER', 'friday': 'INTEGER', 'saturday': 'INTEGER', 'sunday': 'INTEGER', 'start_date': 'CHAR(8)', 'end_date': 'CHAR(8)' }
calendar_dates_txt = {'service_id': 'VARCHAR', 'date': 'CHAR(8)', 'exception_type': 'INTEGER'}
feed_info_txt = {'feed_publisher_name': 'VARCHAR', 'feed_publisher_url': 'VARCHAR', 'feed_lang': 'VARCHAR', 'default_lang': 'VARCHAR', 'feed_start_date': 'CHAR(8)', 'feed_end_date': 'CHAR(8)', 'feed_version': 'VARCHAR', 'feed_contact_email': 'VARCHAR', 'feed_contact_url': 'VARCHAR'}
shapes_txt = {'shape_id': 'VARCHAR', 'shape_pt_lat': 'FLOAT', 'shape_pt_lon': 'FLOAT', 'shape_pt_sequence': 'INTEGER', 'shape_dist_traveled': 'FLOAT'}
transfers_txt = {'from_stop_id': 'VARCHAR', 'to_stop_id': 'VARCHAR', 'from_route_id': 'VARCHAR', 'to_route_id': 'VARCHAR', 'from_trip_id': 'VARCHAR', 'to_trip_id': 'VARCHAR', 'transfer_type': 'INTEGER', 'min_transfer_time': 'INTEGER'}
levels_txt = {'level_id': 'VARCHAR', 'level_index': 'FLOAT', 'level_name': 'VARCHAR'}
frequencies_txt = {'trip_id': 'VARCHAR','start_time': 'VARCHAR','end_time': 'VARCHAR','headway_secs': 'INTEGER', 'exact_times': 'INTEGER'}
pathways_txt = {'pathway_id': 'VARCHAR','from_stop_id': 'VARCHAR','to_stop_id': 'VARCHAR','pathway_mode': 'INTEGER','is_bidirectional': 'INTEGER','length': 'FLOAT','traversal_time': 'INTEGER','stair_count': 'INTEGER','max_slope': 'FLOAT','min_width': 'FLOAT','signposted_as': 'VARCHAR','reversed_signposted_as': 'VARCHAR'}

# Example usage
column_mapping = {
    'stop_lat': 'FLOAT',
    'stop_lon': 'FLOAT',
    'location_type': 'INTEGER',
    'wheelchair_boarding': 'INTEGER',
    'route_type': 'INTEGER',
    'continuous_pickup': 'INTEGER',
    'continuous_drop_off': 'INTEGER',
    'direction_id': 'INTEGER',
    'bikes_allowed': 'INTEGER',
    'arrival_time': 'VARCHAR(8)',
    'departure_time': 'VARCHAR(8)',
    'start_pickup_drop_off_window': 'VARCHAR(8)',
    'end_pickup_drop_off_window': 'VARCHAR(8)',
    'start_time': 'VARCHAR(8)',
    'end_time': 'VARCHAR(8)',
    'prior_notice_last_time': 'VARCHAR(8)',
    'prior_notice_start_time': 'VARCHAR(8)',
    'pickup_type': 'INTEGER',
    'drop_off_type': 'INTEGER',
    'shape_dist_traveled': 'FLOAT',
    'timepoint': 'INTEGER',
    'monday': 'INTEGER',
    'tuesday': 'INTEGER',
    'wednesday': 'INTEGER',
    'thursday': 'INTEGER',
    'friday': 'INTEGER',
    'saturday': 'INTEGER',
    'sunday': 'INTEGER',
    'start_date': 'VARCHAR(8)',
    'end_date': 'VARCHAR(8)',
    'date': 'VARCHAR(8)',
    'exception_type': 'INTEGER',
    'price': 'FLOAT',
    'payment_method': 'INTEGER',
    'transfers': 'INTEGER',
    'transfer_duration': 'INTEGER',
    'fare_media_type': 'INTEGER',
    'amount': 'FLOAT',
    'transfer_count': 'INTEGER',
    'duration_limit': 'INTEGER',
    'duration_limit_type': 'INTEGER',
    'fare_transfer_type': 'INTEGER',
    'shape_pt_lat': 'FLOAT',
    'shape_pt_lon': 'FLOAT',
    'shape_pt_sequence': 'INTEGER',
    'headway_secs': 'INTEGER',
    'exact_times': 'INTEGER',
    'transfer_type': 'INTEGER',
    'min_transfer_time': 'INTEGER',
    'pathway_mode': 'INTEGER',
    'is_bidirectional': 'INTEGER',
    'length': 'FLOAT',
    'traversal_time': 'INTEGER',
    'stair_count': 'INTEGER',
    'max_slope': 'FLOAT',
    'min_width': 'FLOAT',
    'level_index': 'FLOAT',
    'booking_type': 'INTEGER',
    'prior_notice_duration_min': 'INTEGER',
    'prior_notice_duration_max': 'INTEGER',
    'prior_notice_last_day': 'INTEGER',
    'prior_notice_start_day': 'INTEGER',
    'feed_start_date': 'VARCHAR(8)',
    'feed_end_date': 'VARCHAR(8)',
    'is_producer': 'INTEGER',
    'is_operator': 'INTEGER',
    'is_authority': 'INTEGER'
}

import os
import json
from chardet.universaldetector import UniversalDetector


def handle_file(filename: str, column_mapping: dict):
    table = filename.split('/')[-1].replace('.txt', '')
    con = duckdb.connect(database=DUCKDB)
    with duckdb.cursor(con) as cur:
        cur.execute(f"""DROP TABLE IF EXISTS {table};""")

        if os.path.isfile(filename):
            detector = UniversalDetector()
            for line in open(filename, 'rb'):
                detector.feed(line)
                if detector.done: break
            detector.close()

            with open(filename, mode='r', encoding=detector.result['encoding']) as f:
                reader = csv.reader(f)
                header = next(reader)

            if detector.result['encoding'].lower() not in ('utf-8', 'utf-8-sig,', 'ascii'):
                with open(filename, 'r', encoding=detector.result['encoding']) as f_in, open("_tmp", 'w', encoding='UTF-8') as f_out:
                    f_out.writelines(f_in)
                filename = '_tmp'

            this_mapping = {}
            for column in header:
                this_mapping[column] = column_mapping.get(column, 'VARCHAR')

            missing_mapping = {}
            for column in column_mapping.keys() - this_mapping.keys():
                missing_mapping[column] = column_mapping.get(column, 'VARCHAR')

            this_mapping_str = json.dumps(this_mapping)

            cur.execute(f"""CREATE TABLE {table} AS SELECT * FROM read_csv('{filename}', delim=',', header=true, auto_detect=true, columns = {this_mapping_str});""")

            if filename == '_tmp':
                os.remove('_tmp')

            for column in column_mapping.keys() - this_mapping.keys():
                datatype = column_mapping.get(column, 'VARCHAR')
                cur.execute(f"""ALTER TABLE {table} ADD COLUMN {column} {datatype};""")

        else:
            data_types = []
            for column in column_mapping.keys():
                datatype = column_mapping.get(column, 'VARCHAR')
                data_types.append(f"{column} {datatype}")

            data_types = ', '.join(data_types)

            cur.execute(f"""CREATE TABLE {table} ({data_types});""")

    con.close()

base_path = BASEDIR
handle_file(base_path + 'gtfs/feed_info.txt', feed_info_txt)
handle_file(base_path + 'gtfs/agency.txt', agency_txt)
handle_file(base_path + 'gtfs/calendar_dates.txt', calendar_dates_txt)
handle_file(base_path + 'gtfs/calendar.txt', calendar_txt)
handle_file(base_path + 'gtfs/routes.txt', routes_txt)
handle_file(base_path + 'gtfs/levels.txt', levels_txt)
handle_file(base_path + 'gtfs/stops.txt', stops_txt)
handle_file(base_path + 'gtfs/shapes.txt', shapes_txt)
handle_file(base_path + 'gtfs/trips.txt', trips_txt)
handle_file(base_path + 'gtfs/transfers.txt', transfers_txt)
handle_file(base_path + 'gtfs/stop_times.txt', stop_times_txt)
handle_file(base_path + 'gtfs/frequencies.txt', frequencies_txt)
handle_file(base_path + 'gtfs/pathways.txt', pathways_txt)
