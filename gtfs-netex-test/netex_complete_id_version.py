from lxml import etree



def main(inputfile,outputfile):
    # XML file path
    xml_file = inputfile

    # Ignore list of element names
    todoelementlist = ['TimetableFrame','NoticeAssignment','Call', 'TrainNumber']


    # Parse the XML file
    tree = etree.parse(xml_file)

    # Find elements without a version attribute
    elements = tree.xpath('//*[@version=""]')

    # Modify elements by adding a version attribute
    for element in elements:
        if element.tag in todoelementlist:
            element.set('version', 'any')

    # Find elements without an id attribute
    elements_without_id = tree.xpath('//*[@id=""]')

    # Modify elements by adding an id attribute
    for i, element in enumerate(elements_without_id, start=1):
        if element.tag in todoelementlist:
            element.set('id', f'{element.tag}_{i}')

    # Write modified XML back to disk
    tree.write(outputfile, encoding='UTF-8', xml_declaration=True)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx id/version completer. Makes sure that all elements have id and a version')
    parser.add_argument('inputfile', type=str, help='NeTEx file to process')
    parser.add_argument('outputfile', type=str, help='NeTEx file to write to')
    args = parser.parse_args()

    main(args.inputfile,args.outputfile)