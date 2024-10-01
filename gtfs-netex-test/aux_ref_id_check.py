import xml.etree.ElementTree as ET
from anyintodbnew import  open_netex_file
# The script creates a dict of all id and refs (with version and order)
# it the maps

def main(netex_file: str):
    id_dict = {}  # all ids with version, order and type
    ref_dict = {} # all refs with version, order and type
    error_dict = {} # the problems

    for file in open_netex_file(netex_file):
        # Load the XML document
        tree=ET.parse(file)
        root=tree.getroot()
        # Iterate over each element
        for element in root.iter():
            # Extract attributes into a dictionary
            attributes = {attr: value for attr, value in element.attrib.items()}
            attributes.update({"tag": element.tag})
            # Concatenate attributes into a string
            key = '_'.join(sorted(attributes.keys()))
            # Store the attributes in the dictionary
            if not 'version' in element.attrib:
                # if version does not exist, we will add a MPME
                element.attrib['version'] = "NONE"
            if not 'order' in element.attrib:
                # if order does not exist, we will add a NONE
                element.attrib['order'] = "NONE"
            if 'id' in element.attrib:
                key = f"{element.attrib['id']}_{element.attrib['version']}_{element.attrib['order']}"
                id_dict[key] = attributes
            elif 'ref' in element.attrib:
                key = f"{element.attrib['ref']}_{element.attrib['version']}_{element.attrib['order']}"
                ref_dict[key] = attributes
            else:
                # here everything else could be handled, but we will just leave it
                continue

    # build a set of the id values alone
    id_set = []
    for key, idel in id_dict.items():
        id_set.append(idel['id'])
    # match the refs
    for key, ref in ref_dict.items():
        if not id_dict.get(key):
            # no direct match, but perhaps id alone work
            if not key in id_set:
                ref['severity'] = "ID_NOT_FOUND"
                error_dict['key'] = ref
            else:
                ref['severity'] = "ID_VERSION_ORDER_COMBO_NOT_FOUND"
                error_dict['key'] = ref
    # output the results
    print(f"Problematic refs in file{netex_file}")
    print(error_dict)
    print(f'"ref","version","order","class","severity"')
    for key,element in error_dict.items():
        print (f'"{element.get("ref")}","{element.get('version')}","{element.get('order')}","{element.get('tag')}","{element.get('severity')}"')



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx id-ref-checker. Returns a CSV like output')
    parser.add_argument('file', type=str, help='NeTEx file to process')
    # TODO Output to file in a future version
    # parser.add_argument('--csv', type=str, help='Path to the CSV file')
    # parser.add_argument('--fix', action='store_true', help='Fix stuff: Will add version and order to match ref')

    args = parser.parse_args()

    main(args.file)