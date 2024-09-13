import folium
import pandas as pd
import zipfile
import random


# Generate a random dark color
def generate_random_dark_color():
    r = random.randint(0, 200)  # Random red component (0-128)
    g = random.randint(0, 200)  # Random green component (0-128)
    b = random.randint(0, 200)  # Random blue component (0-128)
    return '#%02x%02x%02x' % (r, g, b)
def main(gtfs_zip_file,map_file,write_type):
    # Read GTFS files using pandas
    # Read the GTFS files directly from the ZIP archive using pandas
    with zipfile.ZipFile(gtfs_zip_file, 'r') as zip_ref:
        df_routes = pd.read_csv(zip_ref.open('routes.txt'), usecols=['route_id', 'route_short_name'])
        df_stops = pd.read_csv(zip_ref.open('stops.txt'), usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        df_trips = pd.read_csv(zip_ref.open('trips.txt'), usecols=['route_id', 'trip_id'])
        df_stop_times = pd.read_csv(zip_ref.open('stop_times.txt'), usecols=['trip_id', 'stop_id', 'stop_sequence'])

    # Create a map using Leaflet
    map_center = [df_stops['stop_lat'].mean(), df_stops['stop_lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each stop
    if write_type=="all" or write_type=="stops":
        for _, stop in df_stops.iterrows():
            folium.Marker(
                location=[stop['stop_lat'], stop['stop_lon']],
                popup=stop['stop_name']
            ).add_to(m)


    # Add polylines for each route
    if write_type=="all" or write_type=="routes":
        for _, route in df_routes.iterrows():
            route_id = route['route_id']
            route_trips = df_trips[df_trips['route_id'] == route_id]['trip_id']
            route_stops = df_stop_times[df_stop_times['trip_id'].isin(route_trips)]['stop_id'].unique().tolist()
            route_stop_coords = []
            for astop in route_stops:
                x = df_stops[df_stops['stop_id'] == str(astop)]
                if not (len(x['stop_lat']) == 0 or len(x['stop_lon']) == 0):  # fix for non-existing coordinates
                    if not (x['stop_lat'].values[
                                0] == 0):  # fix for coordinates set to the equator (also bad in our case)
                        # the route osnly for reasonable set stops.
                        route_stop_coords.append([x['stop_lat'].values[0], x['stop_lon'].values[0]])
                    else:
                        print(f'Warning: no valid coordinates for stop {df_stops['stop_id']}')
                else:
                    print(f'Warning: no coordinates for stop {df_stops['stop_id']}')
            if len(route_stop_coords) == 0:
                print(f"route {route_id} has no valid stop sequence.")
                continue
            folium.PolyLine(
                locations=route_stop_coords,
                color=generate_random_dark_color(),
                weight=4,
                opacity=0.8,
                popup=route['route_short_name']
            ).add_to(m)


    # Save the map to an HTML file

    m.save(map_file)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Writes  an html file with leaflet to show')
    parser.add_argument('gtfs_zip_file', type=str, help='GTFS zip file')
    parser.add_argument('map_file', type=str, help='output file (.html)')
    parser.add_argument('write_type', type=str, help='all, stops, routes')

    args = parser.parse_args()

    main(args.gtfs_zip_file,args.map_file,args.write_type)