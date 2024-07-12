import glob

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers.tree import TreeSerializer

from netex import ServiceFrame, ServiceJourney


def conversion(input_filename: str):
    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
    tree = lxml.etree.parse(input_filename)

    with open('/tmp/netex-service-journey.csv', 'a') as o:
        for x in tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourney"):
            service_journey: ServiceJourney
            service_journey = parser.parse(x, ServiceJourney)
            o.write('|'.join([service_journey.id.split(':')[-1].split('-')[0], service_journey.private_code.value]) + "\n")

    # tree.tostring(service_journey, pretty_print=True, strip_text=True)

if __name__ == '__main__':
    with open('/tmp/netex-service-journey.csv', 'w') as o:
        o.write("line|journeynumber\n")

    for input_filename in glob.glob("/tmp/NeTEx_CXX_*.xml.gz"):
        conversion(input_filename)
