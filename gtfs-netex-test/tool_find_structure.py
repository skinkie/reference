# this script allows for finding structure sequences from a folder of XMLs.
# for example, you can search for all XML files that contain PublicationDelivery followed by PublicationTimestamp
# or if requested when searching for PublicationTimestamp -> PublicationDelivery, PublicationTimestamp
# the second path-search use case the code supports allows you to search for example paths for a specific NeTEx element
# for example, you can search for all XML files that contain "ServiceJourney", the code then returns the paths, such as
# ['dataObjects', ',', 'CompositeFrame', ',', 'frames', ',', 'TimetableFrame', ',', 'vehicleJourneys', ',', 'ServiceJourney'] (file1)
# ['dataObjects', ',', 'TimetableFrame', ',', 'vehicleJourneys', ',', 'ServiceJourney'] (file2)
import os

from lxml import etree
from lxml.etree import _Comment


def find_path_in_file(root, to_find, path):
    path_before_loop = path.copy()

    for element in root.findall("*"):
        # skip comments
        if type(element) == _Comment:
            continue
        elif to_find == element.tag.rpartition('}')[2]:
            path.append(element.tag.rpartition('}')[2])

            return path
        else:
            path.append(element.tag.rpartition('}')[2])

            if len(path) > 0:
                path.append(",")

            path_post = find_path_in_file(element, to_find, path)

            if path_post and (to_find in path_post):
                return path_post
            else:
                if len(path) > 1:
                    path = path[0:(len(path) - 2)]
                else:
                    path = []
        path = path_before_loop.copy()


def find_sequence_in_file(root, sequence, sequence_position):
    if sequence_position < len(sequence.split(",")):
        sequence_path_element = sequence.split(",")[sequence_position]

        found = False

        for element in root.iter():
            # skip comments
            if type(element) == _Comment:
                continue
            elif sequence_path_element in element.tag.rpartition('}')[2]:
                found = True
                find_sequence_in_file(element, sequence, (sequence_position + 1))

        if not found:
            print("File did not match")
            return
    else:
        print("File matched")
        return


def find_sequence_in_folder(folder, sequence, sequence_or_path):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".xml"):
                xml_file = os.path.join(root, file)
                print("file: " + str(xml_file))
                if "sequence" in sequence_or_path:
                    find_sequence_in_file(etree.parse(xml_file), sequence, 0)
                elif "path" in sequence_or_path:
                    path = find_path_in_file(etree.parse(xml_file), sequence.split(",")[0], [])

                    if path and ((sequence.split(",")[0]) in path):
                        print(path)
                    else:
                        print("element not found")
        for directory in dirs:
            find_sequence_in_folder(directory, sequence, sequence_or_path)


if __name__ == '__main__':
    import argparse

    argument_parser = argparse.ArgumentParser(
        description='Searches for XML sequences in a given folder or returns the path found towards a given element')
    argument_parser.add_argument('folder', type=str, help='The folder containing the xml files to check')
    argument_parser.add_argument('element_sequence', type=str,
                                 help='The sequence of elements to search for or the one element to find paths for')
    argument_parser.add_argument('sequence_or_path', type=str,
                                 help='Whether to search for a "sequence" or for an element and return the "path" to it')
    # argument_parser.add_argument('any_distance', type=bool,
    #                             help='Whether or the sequence can have an arbitrary hierarchical distance in the structure')
    args = argument_parser.parse_args()

    # Fetching the data based on command-line arguments
    find_sequence_in_folder(args.folder, args.element_sequence, args.sequence_or_path)