import re

def add_unique_ids_to_gml(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()

    # Generate unique IDs
    id_counter = 1
    def unique_id(match):
        nonlocal id_counter
        unique_id = f'R{id_counter}'
        id_counter += 1
        return f'gml:id="{unique_id}"'

    # Replace gml:id attributes with unique IDs
    modified_content = re.sub(r'gml:id="[^"]+"', unique_id, content)

    # Write the modified content back to the same file
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Usage example
file_path = 'C:/Users/ue71603/MG_Daten/github/reference1/gtfs-netex-test/aux_test_input/it-itc4-net_151.xml'
add_unique_ids_to_gml(file_path)