import random
import time
import zipfile

import folium
import pandas as pd
from folium.plugins import MarkerCluster


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
    print("files read in " + str(round(end_time - start_time, 2)))

    # Create a map using Leaflet
    map_center = [47.368650, 8.539183]  # df_stops['stop_lat'].mean(), df_stops['stop_lon'].mean()]
    m = folium.Map(
        location=map_center,
        zoom_start=16
    )
    start_time = time.time()
    print("basemap created in " + str(round(start_time - end_time, 2)))

    # Add markers for each stop - create a dictionary for fast stop lookups
    stop_dict = df_stops.set_index('stop_id')[['stop_lat', 'stop_lon']].T.to_dict('list')
    stop_name_dict = df_stops.set_index('stop_id')[['stop_name']].T.to_dict('list')
    stop_id_duplicates = []

    marker_cluster = MarkerCluster(
        name='Stops',
        overlay=True,
        control=True,
        show=True,
        icon_create_function=None
    ).add_to(m)

    for stop_id, (lat, lon) in stop_dict.items():
        # this loop ensures that we do not have duplicate markers
        if stop_id in stop_id_duplicates:
            continue

        for stop_id_inner, (lat_inner, lon_inner) in stop_dict.items():
            if (lat == lat_inner) & (lon == lon_inner):
                if stop_id == stop_id_inner:
                    continue
                elif stop_id != stop_id_inner:
                    stop_id = stop_id_inner
                    stop_id_duplicates.append(stop_id_inner)
                    break
        folium.Marker(
            location=[lat, lon],
            popup=str(stop_id) + ":" + str(stop_name_dict[stop_id])  # stop_name
        ).add_to(marker_cluster)

    marker_cluster.add_to(m)
    folium.LayerControl().add_to(m)

    end_time = time.time()
    print("markers added for each stop in " + str(round(end_time - start_time, 2)))

    # Create dictionaries for trips creation as well
    # trips_group = folium.FeatureGroup(
    #     name="Trips",
    #     overlay=True,
    #     control=True,
    #     show=False
    # ).add_to(m)
    #
    # route_dict = df_routes.set_index('route_id')[['route_short_name']].T.to_dict('list')
    #
    # trips_dict = df_trips.groupby('route_id')['trip_id'].agg(list).reset_index().set_index('route_id')[
    #     'trip_id'].to_dict()
    #
    # stop_times_dict = df_stop_times.groupby('trip_id')['stop_id'].agg(list).reset_index().set_index('trip_id')[
    #     'stop_id'].to_dict()
    #
    # # Add trips to map
    # for route_id in route_dict.keys():
    #     route_name = route_dict[route_id]
    #
    #     for trip_id in trips_dict[route_id]:
    #         stop_coords = []
    #
    #         for stop_id in stop_times_dict[trip_id]:
    #             stop_coord = stop_dict[stop_id]
    #
    #             if stop_coord:
    #                 stop_coords.append(stop_coord)
    #
    #         folium.PolyLine(
    #             locations=stop_coords,
    #             popup=route_name,
    #             smooth_factor=10
    #         ).add_to(trips_group)
    #
    # start_time = time.time()
    # print("polylines created in: " + str(round(start_time - end_time, 2)))

    # Save the map to an HTML file
    m.save(map_file)
    print("map created in: " + str(round(time.time() - end_time, 2)))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Writes  an html file with leaflet to show')
    parser.add_argument('gtfs_zip_file', type=str, help='GTFS zip file')
    parser.add_argument('map_file', type=str, help='output file (.html)')
    args = parser.parse_args()

    main(args.gtfs_zip_file, args.map_file)
