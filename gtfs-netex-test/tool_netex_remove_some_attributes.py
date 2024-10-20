import os
import zipfile
import xml.etree.ElementTree as ET
import shutil

def remove_attributes(input_file, output_file):
    # Check if the input is a zip file
    if zipfile.is_zipfile(input_file):
        # Create a temporary directory to extract the input zip
        temp_dir = './temp_dir'
        os.makedirs(temp_dir, exist_ok=True)

        # Extract the XML files from the zip to the temporary directory
        with zipfile.ZipFile(input_file, 'r') as zip_ref:
            xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]
            if not xml_files:
                print("No XML file found in the zip.")
                exit(1)
                return
            for xml_file in xml_files:
                zip_ref.extract(xml_file, temp_dir)

        # Process the extracted XML files
        for xml_file in xml_files:
            xml_path = os.path.join(temp_dir, xml_file)
            process_xml_file(xml_path, output_file)

        # Create a new zip file with the modified XML files
        output_zip = output_file
        with zipfile.ZipFile(output_zip, 'w') as zip_ref:
            for folder_name, subfolders, filenames in os.walk(temp_dir):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_ref.write(file_path, os.path.relpath(file_path, temp_dir))

        # Remove the temporary directory
        shutil.rmtree(temp_dir)
    else:
        # Process a single XML file
        process_xml_file(input_file, output_file)

def process_xml_file(xml_file, output_file):
    # Load the XML document
    tree = ET.parse(xml_file)
    root = tree.getroot()
    attribute_remove = ['dataSourceRef', 'responsibilitySetRef']
    # Iterate over the elements in the XML tree
    for element in root.iter():
        # Remove the specified attributes from each element
        for attribute in attribute_remove:
            element.attrib.pop(attribute, None)

    # Write the modified XML back to file
    tree.write(output_file, encoding='UTF-8', xml_declaration=True, default_namespace=None)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Removes some attributes')
    parser.add_argument('input_file', type=str, help='the input file (.xml or .zip)')
    parser.add_argument('output_file', type=str, help='the output file (xml)')
    args = parser.parse_args()

    remove_attributes(args.input_file , args.output_file)