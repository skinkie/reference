from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml

from netex import StopPlace

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

def get_stop_place_for_quayref(tree, quayref):
    found = tree.find(".//{http://www.netex.org.uk/netex}Quay[@id='" + quayref + "']")
    if found is not None:
        stop_place: StopPlace = parser.parse(found.getparent().getparent(), StopPlace)
        return stop_place
    else:
        print(f"Missing {quayref}")

def main():
    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    tree = lxml.etree.parse("/tmp/NeTEx_DOVA_epiap_20240423013251.xml.gz")
    quayref = 'NL:CHB:Quay:15005330'
    get_stop_place_for_quayref(tree, quayref)


