import xml.etree.ElementTree as ET
import random


def get_random_service_journey_id(tree):
    # Find all ServiceJourney elements in the tree
    service_journey_elements = tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourney")

    # Extract the @id attribute from each ServiceJourney element
    service_journey_ids = [element.get('id') for element in service_journey_elements]

    # Select a random @id from the list
    random_id = random.choice(service_journey_ids)

    return random_id


    # Helper function to recursively traverse and keep referenced elements
def traverse(element, processed_elements,root):
    # Find referenced elements through elements with a ref attribute
    ref_elements = element.findall(".//*[@ref]")

    # Find all child nodes of the element
    child_elements = element.findall(".//*")

    # Combine referenced elements and child elements
    relevant_elements = ref_elements + child_elements

    # Traverse relevant elements recursively
    for relevant_element in relevant_elements:
        element_info = (relevant_element.tag, relevant_element.get('@id'), relevant_element.get('@version'))

        # Skip already processed elements to avoid cycles
        if element_info in processed_elements:
            continue

        processed_elements.append(element_info)

        ref_id = relevant_element.get('ref')
        if ref_id:
            referenced_element = root.find(".//*[@id='{}']".format(ref_id))
            if referenced_element is not None:
                traverse(referenced_element, processed_elements,root)
        else:
            traverse(relevant_element, processed_elements,root)


def reduce_xml_tree(xml_file):
    # Load the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    id=get_random_service_journey_id(tree)  # select one ServiceJourney at random
    # Find the ServiceJourney element with the specified id
    service_journey = root.find(".//*[@id='{}']".format(id))

    # If no ServiceJourney element is found, return None
    if service_journey is None:
        return None


    # Create a list to track processed elements
    processed_elements = []

    # Traverse the ServiceJourney element and referenced elements
    traverse(service_journey, processed_elements,root)

    # Create a new XML tree with only the relevant elements
    reduced_tree = ET.ElementTree(root)

    return reduced_tree


def main(input_file, output_file):
    # Specify the desired id for the ServiceJourney

    # Reduce the XML tree based with a random ServiceJoruney
    reduced_tree = reduce_xml_tree(input_file)

    if reduced_tree is not None:
        # Save the reduced tree to the output file
        reduced_tree.write(output_file)

        print("XML tree reduced and saved to:", output_file)
    else:
        print("Did not work.")




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extracts exactly one ServiceJourney at random from the file.')
    parser.add_argument('input_file', type=str, help='input XML')
    parser.add_argument('output_file', type=str, help='output XML')
    args = parser.parse_args()

    main(args.input_file,args.output_file)