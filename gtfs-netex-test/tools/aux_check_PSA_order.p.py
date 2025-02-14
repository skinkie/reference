import zipfile
import xml.etree.ElementTree as ET

def check_zip_for_illegal_utf8_chars(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for file_name in zip_file.namelist():
            if file_name.endswith('.xml'):
                with zip_file.open(file_name, 'r') as xml_file:
                    try:
                        print(f"checking {file_name}")
                        xml_data = xml_file.read().decode('utf-8')
                        root = ET.fromstring(xml_data)
                        check_element_for_order_attribute(root)
                    except (UnicodeDecodeError, ET.ParseError) as e:
                        print(f"Invalid UTF-8 characters in file: {file_name}")
                        print(f"Error: {str(e)}")

def check_element_for_order_attribute(element):
    if is_passenger_stop_assignment(element):
        print("PSA found.")
        if 'order' not in element.attrib:
            print("The 'PassengerStopAssignment' element does not have an 'order' attribute.")

    for child in element:
        check_element_for_order_attribute(child)

def is_passenger_stop_assignment(element):
    if element.tag.endswith('PassengerStopAssignment') or element.tag.endswith('PassengerStopAssignment'):
        return True
    return False

# Example usage
check_zip_for_illegal_utf8_chars('D:/aux_testing_processing/swiss-prod/swiss.zip')
