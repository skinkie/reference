import os
import zipfile
import xml.etree.ElementTree as ET


# TODO also do a reference check (when version is missing)


def add_id_and_version(input_file, output_file):
    element_names = ['TimetabledPassingTime']  #add other elements when necessary
    if zipfile.is_zipfile(input_file):
        # Input is a zip file
        with zipfile.ZipFile(input_file, 'r') as zip_ref:
            # Extract the XML file from the zip
            xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]
            if not xml_files:
                print("No XML file found in the zip.")
                exit(1)
                return
            elif len(xml_files) > 1:
                print("Multiple XML files found in the zip. Processing the first one.")
            xml_file = xml_files[0]
            zip_ref.extract(xml_file)

        # Process the extracted XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Iterate over the elements in the XML tree
        for sequence, element_name in enumerate(element_names, start=1):
            # Find elements by name
            elements = root.findall('.//{http://www.netex.org.uk/netex}'+element_name)

            # Add id and version attributes if missing
            for element in elements:
                if 'id' not in element.attrib:
                    element.set('id', '{}{}'.format(element_name, sequence))
                if 'version' not in element.attrib:
                    element.set('version', 'any')

        # Write the modified XML back to file
        tree.write(output_file,encoding='UTF-8', xml_declaration=True, default_namespace=None)

        # Remove the extracted XML file
        os.remove(xml_file)
    else:
        # Input is a single XML file
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Iterate over the elements in the XML tree
        for sequence, element_name in enumerate(element_names, start=1):
            # Find elements by name
            elements = root.findall('.//{http://www.netex.org.uk/netex}'+element_name)

            # Add id and version attributes if missing
            for element in elements:
                if 'id' not in element.attrib:
                    element.set('id', '{}{}'.format(element_name, sequence))
                if 'version' not in element.attrib:
                    element.set('version', 'any')

        # Write the modified XML back to file
        tree.write(output_file,encoding='UTF-8', xml_declaration=True, default_namespace=None)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Makes sure that the relevant elements have id and version attributes. Existing ones are kept')
    parser.add_argument('input_file', type=str, help='the input file (.xml or .zip)')
    parser.add_argument('output_file', type=str, help='the output file (xml)')
    args = parser.parse_args()

    add_id_and_version(args.input_file , args.output_file)