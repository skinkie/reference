import os
from lxml import etree

def list_ids_with_version(xml_file, version):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    ids = []
    for element in root.iter():
        if element.get('version') == version:
            id_value = element.get('id')
            if id_value is not None:
                ids.append(id_value)

    return ids

def get_unique_versions_with_ids(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    versions = set()
    version_id_examples = {}

    for element in root.iter():
        version = element.get('version')
        if version is not None:
            versions.add(version)
            if version not in version_id_examples:
                version_id_examples[version] = element.get('id')

    return versions, version_id_examples

# Example usage
xml_file_path = "C:/Users/ue71603/Downloads/lex-20241202020252.xml"

if False:
    unique_versions, version_id_examples = get_unique_versions_with_ids(xml_file_path)

    print("Different versions:")
    for version in unique_versions:
        print(version)

    print("\nExamples of id attributes:")
    for version, example_id in version_id_examples.items():
        print("Version:", version)
        print("Example id:", example_id)
        print()



else:
    version = '1'

    ids_with_version_1 = list_ids_with_version(xml_file_path, version)

    print("IDs with version '1':")
    for id_value in ids_with_version_1:
        print(id_value)

