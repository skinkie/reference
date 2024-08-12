from lxml import etree


def main(xmlschema:str,file: str):
    print("***************************************************")
    print("file: "+file)
    print("schema: "+xmlschema)
    print("***************************************************")

    try:
        schema_doc=etree.parse(xmlschema)
        print("schema parsed.")
        schema = etree.XMLSchema(schema_doc)
        print("schema made ready.")
        print("parsing file.")
        tree = etree.parse(file)
        root = tree.getroot()
        print("file parsed.")
        print("Validation starting")
        schema.assertValid(root)
    except etree.DocumentInvalid as e:
        print ("XML validation error:", e)
    print("***************************************************")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='NeTEx XSD validation')
    parser.add_argument('xmlschema', type=str, help='NeTEx schema to use')
    parser.add_argument('file', type=str, help='NeTEx file to process')
    args = parser.parse_args()

    main(args.xmlschema,args.file)