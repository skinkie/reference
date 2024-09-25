import random
import sys
import time
import zipfile

import folium
import pandas as pd


# Generate a random dark color
def generate_random_dark_color():
    r = random.randint(0, 200)  # Random red component (0-128)
    g = random.randint(0, 200)  # Random green component (0-128)
    b = random.randint(0, 200)  # Random blue component (0-128)
    return '#%02x%02x%02x' % (r, g, b)


def main(gtfs_zip_file, map_file):
    # Read GTFS files using pandas
    # Read the GTFS files directly from the ZIP archive using pandas
    start_time = time.time()
    with zipfile.ZipFile(gtfs_zip_file, 'r') as zip_ref:
        df_routes = pd.read_csv(zip_ref.open('routes.txt'), usecols=['route_id', 'route_short_name'])
        df_stops = pd.read_csv(zip_ref.open('stops.txt'), usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        df_trips = pd.read_csv(zip_ref.open('trips.txt'), usecols=['route_id', 'trip_id', 'trip_headsign'])
        df_stop_times = pd.read_csv(zip_ref.open('stop_times.txt'), usecols=['trip_id', 'stop_id', 'stop_sequence'])
    end_time = time.time()
    print("files read in " + str(end_time - start_time))

    # Create a map using Leaflet
    map_center = [df_stops['stop_lat'].mean(), df_stops['stop_lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=12)
    start_time = time.time()
    print("basemap created in " + str(start_time - end_time))

    # Add markers for each stop
    # Create a dictionary for fast stop lookups
    stop_dict = df_stops.set_index('stop_id')[['stop_lat', 'stop_lon']].T.to_dict('list')  # efficiency improvement #1
    end_time = time.time()
    print("stop_dict in " + str(end_time - start_time))

    for stop_id, (lat, lon) in stop_dict.items():
        folium.Marker(
            location=[lat, lon],
            popup=stop_dict[stop_id][1]  # stop_name
        ).add_to(m)
    start_time = time.time()
    print("Markers added for each stop in " + str(start_time - end_time))

    # Add polylines for each route
    print("Creating polylines for each route. Total values to process: " + str(df_routes.size))

    # Create cache structures - performance #3
    route_dict = df_routes.set_index('route_id')[['route_short_name']].T.to_dict('list')
    end_time = time.time()
    print("route_dict in " + str(end_time - start_time))

    trips_dict = df_trips.groupby('route_id')['trip_id'].agg(list).reset_index().set_index('route_id')[
        'trip_id'].to_dict()
    start_time = time.time()
    print("trips_dict in " + str(start_time - end_time))

    stop_times_dict = df_stop_times.groupby('trip_id')['stop_id'].agg(list).reset_index().set_index('trip_id')[
        'stop_id'].to_dict()
    end_time = time.time()
    print("stop_times_dict in " + str(end_time - start_time))

    # create a map from trip to list of stops
    for route_id in route_dict.keys():
        route_name = route_dict[route_id]

        for trip_id in trips_dict[route_id]:
            stop_coords = []

            for stop_id in stop_times_dict[trip_id]:
                stop_coord = stop_dict[stop_id]

                if stop_coord:
                    stop_coords.append(stop_coord)

            folium.PolyLine(
                locations=stop_coords,
                color=generate_random_dark_color(),
                weight=4,
                opacity=0.8,
                popup=route_name
            ).add_to(m)

    start_time = time.time()
    print("polylines added in: " + str(start_time - end_time))

    # Save the map to an HTML file
    m.save(map_file)
    print("map created in: " + str(time.time() - start_time))


# Function to remove duplicates from each inner list
def remove_duplicates(nested_list):
    unique_nested_list = []
    for inner_list in nested_list:
        # Convert inner lists to tuples to use set for uniqueness
        unique_inner = list(map(list, set(map(tuple, inner_list))))
        unique_nested_list.append(unique_inner)
    return unique_nested_list


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Writes  an html file with leaflet to show')
    parser.add_argument('gtfs_zip_file', type=str, help='GTFS zip file')
    parser.add_argument('map_file', type=str, help='output file (.html)')
    args = parser.parse_args()

    main(args.gtfs_zip_file, args.map_file)
