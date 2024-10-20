import logging
import re
from lxml import etree
from aux_logging import *
import traceback


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
            log_print(f'comment: {comment}')
        elif assertion.startswith('contains'):
            regex = assertion.split(' ', 1)[1]
            if re.search(regex, input_content):
                log_print(f'Assertion PASSed: File contains regex "{regex}"')
            else:
                log_all(logging.ERROR, "assertions", f'Assertion FAILed: File does not contain regex "{regex}"')
                failed=1
        elif assertion.startswith('xpathcountequal'):
            parts = assertion.split(' ')
            xpath_expression = parts[1]
            expected_count = int(parts[2])
            results = tree.xpath(xpath_expression, namespaces=namespaces)
            if len(results) == expected_count:
                log_print(f'Assertion PASSed: XPath "{xpath_expression}" has {expected_count} results')
            else:
                log_all(logging.ERROR, "assertions", f'Assertion FAILed: XPath "{xpath_expression}" does not have {expected_count} results, was {len(results)}')
                failed=1
        elif assertion.startswith('xpathcountgreater'):
            parts = assertion.split(' ')
            xpath_expression = parts[1]
            expected_count = int(parts[2])
            results = tree.xpath(xpath_expression, namespaces=namespaces)
            if len(results) > expected_count:
                log_print(f'Assertion PASSed: XPath "{xpath_expression}" has more than {expected_count} results, was {len(results)}')
            else:
                log_all(logging.ERROR, "assertions", f'Assertion FAILed: XPath "{xpath_expression}" does not have more than {expected_count} results, was {len(results)}')
                failed=1
        elif len(assertion.strip()) > 0:
            log_all(logging.ERROR, "assertions", f'Invalid assertion: {assertion}')
            failed = 1
    if (failed>0):
        exit(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Lets a set of assertions run on a file (xml)')
    parser.add_argument('assertions_file', type=str, help='File with the assertions')
    parser.add_argument('input_file', type=str, help='the input file (xml)')
    parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)
    try:
        process_assertions(args.assertions_file, args.input_file)
        log_flush()
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        log_flush()
        raise e


