import xml.etree.ElementTree as ET


def main(file: str):
    print("***************************************************")
    print("file: "+file)
    print("***************************************************")

    # Load the XML document
    tree=ET.parse(file)
    print(tree)
    root=tree.getroot()
    id_dict = {}
    ref_dict = {}
    error_dict = {}
    # Iterate over each element
    for element in root.iter():
        # Extract attributes into a dictionary
        attributes = {attr: value for attr, value in element.attrib.items()}
        attributes.update({"tag": element.tag})
        # Concatenate attributes into a string
        key = '_'.join(sorted(attributes.keys()))
        # Store the attributes in the dictionary
        if not 'version' in element.attrib:
            element.attrib['version']="NONE"
        if not 'order' in element.attrib:
            element.attrib['order']="NONE"
        if 'id' in element.attrib:
            key = f"{element.attrib['id']}_{element.attrib['version']}_{element.attrib['order']}"
            id_dict[key] = attributes
        elif 'ref' in element.attrib:
            key = f"{element.attrib['ref']}_{element.attrib['version']}_{element.attrib['order']}"
            ref_dict[key] = attributes
        else:
            key = '_'.join(sorted(attributes.keys()))
            error_dict[key] = attributes
    print ("\n\n\nid: \n")
    for element in id_dict:
        print (f"{element}")
    print("\n\n\nref: \n")
    for element in ref_dict:
        print (f"{element}")

    print("\n\n\nerror: \n")
    print(error_dict)
    for element in error_dict:
        print (f"{element}")

    print("\n\n\nCrosschecking:\n")
    for e1 in id_dict:
        if not e1 in ref_dict:
            if id_dict[e1]["tag"] in ["ServiceJourney", "StopPlace","ScheduledStopPoint","Operator","Organisation"]:
                print(f"can be deleted: {e1}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx id-ref-checker')
    parser.add_argument('file', type=str, help='NeTEx file to process')
    args = parser.parse_args()

    main(args.file)