import sys
import xml.etree.ElementTree as ET
from anyintodbnew import  open_netex_file
# The script creates a dict of all id and refs (with version and order)
# it the maps

#TODO missing parent - child relation between SP -> Q, SP -> SP and Q -> Q must be implemented as well

def coordinates_check(netex_file:str, dofail,dofix):
    scheduled_stop_points = {}
    stop_places = {}
    quay_centroids = {}
    passenger_stop_assignments = {}

    # we need two passes
    # 1. pass: builds dicts
    # intermed: spread coordinates in the dicts
    # 2. pass: add coordinates where necessary and store files

    # There are three connections:
    # 1. explicit ParentRef TODO
    # 2. PassengerStopAssignments
    # 3. Implicit defined within Quays within StopPlaces  TODO

    for file in open_netex_file(netex_file):
        print("***************************************************")
        print("file: "+file)
        print("***************************************************")

        # Load the XML document
        tree = ET.parse(file)
        root = tree.getroot()
        # Iterate over each element
        for element in root.iter():
            if element.tag == 'ScheduledStopPoint':
                id = element.attrib.get('id')
                version = element.attrib.get('version')
                coordinates = {
                    'Longitude': None,
                    'Latitude': None,
                    'ParentRef' : None,
                    'Processed' : False
                }
                for child in element.iter():
                    if child.tag == 'Centroid':
                        for sub_child in child.iter():
                            if sub_child.tag == 'Location':
                                for coord in sub_child.iter():
                                    if coord.tag == 'Longitude':
                                        coordinates['Longitude'] = coord.text
                                    elif coord.tag == 'Latitude':
                                        coordinates['Latitude'] = coord.text
                    elif child.tag == 'ParentRef':
                        id = child.attrib.get('id')
                        version = child.attrib.get('version')
                        coordinates['ParentRef'] = f'{id}+{version}'
                scheduled_stop_points[f'{id}+{version}'] = coordinates

            elif element.tag == 'StopPlace':
                id = element.attrib.get('id')
                version = element.attrib.get('version')
                coordinates = {
                    'Longitude': None,
                    'Latitude': None,
                    'ParentRef' : None,
                    'Processed' : False
                }
                for child in element.iter():
                    if child.tag == 'Centroid':
                        for sub_child in child.iter():
                            if sub_child.tag == 'Location':
                                for coord in sub_child.iter():
                                    if coord.tag == 'Longitude':
                                        coordinates['Longitude'] = coord.text
                                    elif coord.tag == 'Latitude':
                                        coordinates['Latitude'] = coord.text
                    elif child.tag == 'ParentRef':
                        id = child.attrib.get('id')
                        version = child.attrib.get('version')
                        coordinates['ParentRef'] = f'{id}+{version}'
                stop_places[f'{id}+{version}'] = coordinates

            elif element.tag == 'Quay':
                id = element.attrib.get('id')
                version = element.attrib.get('version')
                coordinates = {
                    'Longitude': None,
                    'Latitude': None,
                    'ParentRef' : None,
                    'Processed' : False
                }
                for child in element.iter():
                    if child.tag == 'Centroid':
                        for sub_child in child.iter():
                            if sub_child.tag == 'Location':
                                for coord in sub_child.iter():
                                    if coord.tag == 'Longitude':
                                        coordinates['Longitude'] = coord.text
                                    elif coord.tag == 'Latitude':
                                        coordinates['Latitude'] = coord.text
                    elif child.tag == 'ParentRef':
                        id = child.attrib.get('id')
                        version = child.attrib.get('version')
                        coordinates['ParentRef'] = f'{id}+{version}'
                quay_centroids[f'{id}+{version}'] = coordinates
            elif element.tag == 'PassengerStopAssignment':
                quay_ref = None
                quay = None
                stop_place_ref = None
                stop_place = None
                scheduled_stop_point_ref = None
                scheduled_stop_point = None

                for child in element.iter():
                    if child.tag == 'QuayRef':
                        quay_ref = child.attrib.get('ref') + '+' + child.attrib.get('version')
                    elif child.tag == 'Quay':
                        quay = child.attrib.get('id') + '+' + child.attrib.get('version')
                    elif child.tag == 'StopPlaceRef':
                        stop_place_ref = child.attrib.get('ref') + '+' + child.attrib.get('version')
                    elif child.tag == 'StopPlace':
                        stop_place = child.attrib.get('id') + '+' + child.attrib.get('version')
                    elif child.tag == 'ScheduledStopPointRef':
                        scheduled_stop_point_ref = child.attrib.get('ref') + '+' + child.attrib.get('version')
                    elif child.tag == 'ScheduledStopPoint':
                        scheduled_stop_point = child.attrib.get('id') + '+' + child.attrib.get('version')

                passenger_stop_assignments[element.attrib.get('id') + '+' + element.attrib.get('version')] = {
                    'Q': quay_ref or quay,
                    'SP': stop_place_ref or stop_place,
                    'SSP': scheduled_stop_point_ref or scheduled_stop_point
                }

            if not dofix:
                # report state
                for key, element in scheduled_stop_points.items():
                    if 'Longitude' not in element:
                        print(f'"SSP","{key}"')
                        if dofail:
                            sys.exit(2)
                for key, element in stop_places.items():
                    if 'Longitude' not in element:
                        print(f'"SP","{key}"')
                        if dofail:
                            sys.exit(2)
                for key, element in quay_centroids.items():
                    if 'Longitude' not in element:
                        print(f'"Quay","{key}"')
                        if dofail:
                            sys.exit(2)
                return



            # 1. Propagate coordinates from Quay to Quay, where necessary (TODO when we do parent relationship)
            # 2. Propagate coordinates from Quay to SP, where necessary (TODO when we do parent relationship)
            # 3. Propagate coordinates from SP to Quay, where necessary (TODO when we do parent relationship)
            # 4. Propagate coordinates from SP to SP, where necessary (TODO when we do parent relationship)

            for assignment in passenger_stop_assignments:
                Q = assignment.get('key')
                SP = assignment.get('key')
                SSP = assignment.get('key')

                # 5. Propagate coordinates from Quay to SSP, where necessary
                if scheduled_stop_points[SSP] and scheduled_stop_points[SSP].get('Longitude') is None and quay_centroids[Q] and quay_centroids[Q].get('Longitude'):
                    scheduled_stop_points[SSP]['Longitude'] = quay_centroids[Q]['Longitude']
                    scheduled_stop_points[SSP]['Latitude'] = quay_centroids[Q]['Latitude']
                    scheduled_stop_points[SSP]['Processed'] = True

                # 6. Propagate coordinates from StopPlace to SSP, where necessary
                if scheduled_stop_points[SSP] and scheduled_stop_points[SSP].get('Longitude') is None and stop_places[SP] and stop_places[SP].get('Longitude'):
                    scheduled_stop_points[SSP]['Longitude'] = stop_places[SP]['Longitude']
                    scheduled_stop_points[SSP]['Latitude'] = stop_places[SP]['Latitude']
                    scheduled_stop_points[SSP]['Processed'] = True


                # 7. Propagate coordinates from SSP to Quay, where necessary
                if quay_centroids[Q] and quay_centroids[Q].get('Longitude') is None and scheduled_stop_points[SSP] and scheduled_stop_points[SSP].get('Longitude'):
                    quay_centroids[Q]['Longitude'] = scheduled_stop_points[SSP]['Longitude']
                    quay_centroids[Q]['Latitude'] = scheduled_stop_points[SSP]['Latitude']
                    quay_centroids[Q]['Processed'] = True

                # 8. Propagate coordinates from SSP to SP, where necessary
                if stop_places[SP] and stop_places[SP].get('Longitude') is None and scheduled_stop_points[SSP] and scheduled_stop_points[SSP].get('Longitude'):
                    stop_places[SP]['Longitude'] = scheduled_stop_points[SSP]['Longitude']
                    stop_places[SP]['Latitude'] = scheduled_stop_points[SSP]['Latitude']
                    stop_places[SP]['Processed'] = True

            # Work again through the files and write back new
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx adds coordinates to StopPlace, Quay and ScheduledStopPoint')
    parser.add_argument('file', type=str, help='NeTEx file to process (xml, zip or gzip')
    parser.add_argument('--fix', action='store_true', help='tries to spread coordinates')
    parser.add_argument('--fail', action='store_true', help='fails if missing a coordinate')

    args = parser.parse_args()

    coordinates_check(args.file,args.fail,args.fix)