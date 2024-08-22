import re
from lxml import etree

def process_assertions(assertions_file, input_file):
    tree = etree.parse(input_file)
    # Define the namespace URI
    namespace_uri = 'http://www.netex.org.uk/netex'

    # Create the namespace map with the URI as the value
    namespaces = {'netex': namespace_uri}
    with open(input_file, 'r',encoding='utf-8') as file:
        input_content = file.read()

    with open(assertions_file, 'r') as file:
        assertions = file.readlines()
    failed=0
    for assertion in assertions:
        assertion = assertion.strip()
        if assertion.startswith('#'):
            comment = assertion.split(' ', 1)[1]
            print(f'comment: {comment}')
        elif assertion.startswith('contains'):
            regex = assertion.split(' ', 1)[1]
            if re.search(regex, input_content):
                print(f'Assertion PASSed: File contains regex "{regex}"')
            else:
                print(f'Assertion FAILed: File does not contain regex "{regex}"')
                failed=1
        elif assertion.startswith('xpathcountequal'):
            parts = assertion.split(' ')
            xpath_expression = parts[1]
            expected_count = int(parts[2])
            results = tree.xpath(xpath_expression, namespaces=namespaces)
            if len(results) == expected_count:
                print(f'Assertion PASSed: XPath "{xpath_expression}" has {expected_count} results')
            else:
                print(f'Assertion FAILed: XPath "{xpath_expression}" does not have {expected_count} results, was {len(results)}')
                failed=1
        elif assertion.startswith('xpathcountgreater'):
            parts = assertion.split(' ')
            xpath_expression = parts[1]
            expected_count = int(parts[2])
            results = tree.xpath(xpath_expression, namespaces=namespaces)
            if len(results) > expected_count:
                print(f'Assertion PASSed: XPath "{xpath_expression}" has more than {expected_count} results, was {len(results)}')
            else:
                print(f'Assertion FAILed: XPath "{xpath_expression}" does not have more than {expected_count} results, was {len(results)}')
                failed=1
        else:
            print(f'Invalid assertion: {assertion}')
    if (failed>0):
        exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Lets a set of assertions run on a file (xml)')
    parser.add_argument('assertions_file', type=str, help='File with the assertions')
    parser.add_argument('input_file', type=str, help='the input file (xml)')
    args = parser.parse_args()
    process_assertions(args.assertions_file, args.input_file)
