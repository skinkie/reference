import random
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
    with zipfile.ZipFile(gtfs_zip_file, 'r') as zip_ref:
        df_routes = pd.read_csv(zip_ref.open('routes.txt'), usecols=['route_id', 'route_short_name'])
        df_stops = pd.read_csv(zip_ref.open('stops.txt'), usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        df_trips = pd.read_csv(zip_ref.open('trips.txt'), usecols=['route_id', 'trip_id'])
        df_stop_times = pd.read_csv(zip_ref.open('stop_times.txt'), usecols=['trip_id', 'stop_id', 'stop_sequence'])
    print("files read")

    # Create a map using Leaflet
    map_center = [df_stops['stop_lat'].mean(), df_stops['stop_lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=12)
    print("basemap created")

    # Add markers for each stop
    # Create a dictionary for fast stop lookups
    stop_dict = df_stops.set_index('stop_id')[['stop_lat', 'stop_lon']].T.to_dict('list')  # efficiency improvement #1

    for stop_id, (lat, lon) in stop_dict.items():
        folium.Marker(
            location=[lat, lon],
            popup=stop_dict[stop_id][1]  # stop_name
        ).add_to(m)
    print("Markers added for each stop")

    # Add polylines for each route
    print("Creating polylines for each route. Total values to process: " + str(df_routes.size))

    # List to cache route stop coordinates and corresponding route information - efficiency improvement #2
    route_info_coords = []
    route_info_popups = []

    df_routes

    for idx, route in df_routes.iterrows():
        route_id = route['route_id']
        route_trips = df_trips[df_trips['route_id'] == route_id]['trip_id']

        route_stops = df_stop_times[df_stop_times['trip_id'].isin(route_trips)]['stop_id'].unique()

        route_stop_coords = [stop_dict[stop] for stop in route_stops if stop in stop_dict]

        if not route_stop_coords:
            print(f"Route {route_id} has no valid stop sequence.")
            continue

        route_info_coords.append(route_stop_coords)
        route_info_popups.append(route['route_short_name'])

    # related to efficiency improvement #2
    print("creating mape")
    i = 0
    for info in route_info_coords:
        folium.PolyLine(
            locations=info,
            color=generate_random_dark_color(),
            weight=4,
            opacity=0.8,
            popup=route_info_popups[i]
        ).add_to(m)

    # Save the map to an HTML file
    m.save(map_file)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Writes  an html file with leaflet to show')
    parser.add_argument('gtfs_zip_file', type=str, help='GTFS zip file')
    parser.add_argument('map_file', type=str, help='output file (.html)')
    args = parser.parse_args()

    main(args.gtfs_zip_file, args.map_file)
