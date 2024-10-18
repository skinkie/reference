import os
import zipfile
from lxml import etree

def find_duplicates(input_file):
    # Create a list to store elements with duplicate combinations
    duplicates = []

    if zipfile.is_zipfile(input_file):
        # Input is a ZIP archive
        with zipfile.ZipFile(input_file, 'r') as zip_ref:
            xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]
            for xml_file in xml_files:
                # Process each XML file within the ZIP archive
                print(f"Processing: {xml_file}")
                xml_content = zip_ref.read(xml_file)
                process_xml_content(xml_content, duplicates,xml_file)
    else:
        # Input is a single XML file
        with open(input_file, 'rb') as file:
            xml_content = file.read()
            process_xml_content(xml_content, duplicates,input_file)

    # Print the elements with duplicate combinations
    for element, filename in duplicates:
        print(f"{filename}: {etree.tostring(element).decode()}")
    if len(duplicates)>0:
        exit(1)

def process_xml_content(xml_content, duplicates,file):
    # Parse the XML content
    tree = etree.fromstring(xml_content)

    # Iterate over the elements in the XML tree
    elements = tree.xpath('.//*[@id and @version]')
    combinations = set()
    for element in elements:
        # Check for duplicate combinations of id and version attributes
        combination = (element.get('id'), element.get('version'))
        if combination in combinations:
            duplicates.append([element,file])
            print(f"duplicate found: {element.get('id')} - {element.get('version')}")
        else:
            combinations.add(combination)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Checks for duplicate id/version in file')
    parser.add_argument('input_file', type=str, help='Input NeTEx file xml ord zip.')
    args = parser.parse_args()

    find_duplicates(args.input_file)
