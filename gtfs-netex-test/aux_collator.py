# Autocollator
import xml.etree.ElementTree as ET
import zipfile

def get_text_from_last(input_string, search_string):
    index = input_string.rfind(search_string)
    if index != -1:
        return input_string[index:]
    else:
        return input_string


def get_text_until(input_string, search_string):
    index = input_string.find(search_string)
    if index != -1:
        return input_string[:index + len(search_string)]
    else:
        return input_string


def read_file_to_string(file_name):
    with open(file_name, 'r',encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents
def extract_xml_sections(file_path):
    # Check if the file_path is a zip file
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Get the list of files in the zip
            file_list = zip_ref.namelist()

            # Find the first XML file in the zip
            xml_file = next((file for file in file_list if file.endswith('.xml')), None)

            if xml_file:
                # Extract the XML file from the zip
                zip_ref.extract(xml_file)
                extracted_file_path = xml_file
            else:
                raise ValueError("No XML files found in the zip.")

    else:
        extracted_file_path = file_path

    mystring=read_file_to_string(extracted_file_path)

    # Extract everything before and including <frames>
    string_file_begin = get_text_until(mystring, "<frames>")

    # Extract everything including </frames>
    string_file_end = get_text_from_last(mystring,"</frames>")

    return string_file_begin, string_file_end

def extract_frames_from_zip(zip_file_path, output_file):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()

        for file_name in file_list:
            if file_name.endswith('.xml'):
                with zip_ref.open(file_name, 'r') as xml_file:
                    print(f'Processing: {file_name}')
                    # Parse the XML file
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    # Remove namespaces from the XML tree
                    remove_namespaces(root)

                    # Find the <frames> element
                    frames_element = root.find('.//frames')

                    if frames_element is not None:
                        content = ''.join(ET.tostring(child, encoding='unicode') for child in frames_element)

                        # Write the content to the output file
                        output_file.write(content)


def remove_namespaces(element):
  for elem in element.iter():
    if '}' in elem.tag:
      elem.tag = elem.tag.split('}', 1)[1]

def main(input_file,output_file):
    preamble, postamble = extract_xml_sections(input_file)
    with open(output_file,'w',encoding='utf-8') as out:
        out.write(preamble)
        extract_frames_from_zip(input_file,out)
        out.write(postamble)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Makes one big NeTEx file out of several smaller ones (simple only)')
    parser.add_argument('input_file', type=str, help='input zip')
    parser.add_argument('output_file', type=str, help='collated output xml')
    args = parser.parse_args()

    main(args.input_file,args.output_file)