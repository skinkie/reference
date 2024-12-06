import xml.etree.ElementTree as ET
import openpyxl




def deduplicate_xml_file(xml_file_path, output_file_path,warning_excel):
    # Create an Excel workbook and sheet for writing warnings
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['Type', 'ID', 'Version', 'First 10 Lines'])

    # Create a set to store processed elements
    processed_elements = set()

    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through all elements
    for element in root.iter():
        element_type = element.get('type')
        element_id = element.get('id')
        element_version = element.get('version')


        # Check if the element is a duplicate
        if (element_type, element_id, element_version) in processed_elements:
            element_xml = ET.tostring(element, encoding='unicode')
            sheet.append([element_type, element_id, element_version, element_xml[:10]])
            # Remove the duplicate element
            root.remove(element)
        else:
            # Add the element to the set of processed elements
            processed_elements.add((element_type, element_id, element_version))

    # Write the deduplicated XML content to the output file
    tree.write(output_file_path)

    # Save the warnings to the Excel file
    workbook.save(warning_excel)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Checks for duplicates in elements and writes an error list and a deduplicated file.')
    parser.add_argument('input_file', type=str, help='input XML')
    parser.add_argument('output_file', type=str, help='outputXML')
    parser.add_argument('warnings_file', type=str, help='xlsx with problems')
    args = parser.parse_args()

    deduplicate_xml_file(args.input_file,args.output_file,args.output_file)

