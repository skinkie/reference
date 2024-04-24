from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import LxmlTreeSerializer

from netex import ServiceFrame

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

tree = lxml.etree.parse("NeTEx_WSF_WSF_20240415_20240415.xml.gz")

service_frame: ServiceFrame

for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceFrame"):
    service_frame = parser.parse(element, ServiceFrame)

lxml_serializer = LxmlTreeSerializer(context)

# tree = lxml.etree.parse("/tmp/NeTEx_WSF_WSF_20240415_20240415.xml.gz")

element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
element.getparent().replace(element, lxml_serializer.render(service_frame))

tree.write("test-output.xml", pretty_print=True, strip_text=True)