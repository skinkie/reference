# @https://github.com/ue71603, 2024
import os

from lxml import etree


def check_xsd_validity(xsd_file):
    try:
        etree.parse(xsd_file)
        print(f"{xsd_file} is a valid XSD file")
    except etree.XMLSyntaxError as e:
        print(f"{xsd_file} is an invalid XSD file: {str(e)}")
    except Exception as e:
        print(f"An error occurred while checking {xsd_file}: {str(e)}")


def validate_xml(xml_file, xmlschema):
    try:
        xmlschema.assertValid(etree.parse(xml_file))
        print(f"{xml_file} is valid against {xmlschema}")
    except etree.XMLSchemaError as e:
        print(f"{xml_file} is invalid: {str(e)}")
    except Exception as e:
        print(f"An error occurred while validating {xml_file}: {str(e)}")


def validate_xsd_in_folder(folder, xsd_schema):
    xmlschema = etree.XMLSchema(etree.parse(xsd_schema))
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".xml"):
                xsd_file = os.path.join(root, file)
                validate_xml(xsd_file, xmlschema)
            if file.endswith(".xsd"):
                xsd_file = os.path.join(root, file)
                check_xsd_validity(xsd_file)


if __name__ == '__main__':
    import argparse

    argument_parser = argparse.ArgumentParser(description='Validates each file in a folder (xsd and xml)')
    argument_parser.add_argument('folder', type=str, help='The folder containing the xml files to validate')
    argument_parser.add_argument('xmlschema', type=str, help='The schema file to use as a basis for validation')
    args = argument_parser.parse_args()

    # Fetching the data based on command-line arguments
    validate_xsd_in_folder(args.folder, args.xmlschema)
