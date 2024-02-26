from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import lxml

from netex import RouteLink

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

tree = lxml.etree.parse("/tmp/NeTEx_CXX_HWGO_20240213_2024-02-18_202400046_baseline.xml.gz")

for element in tree.iterfind(".//{http://www.netex.org.uk/netex}RouteLink"):
    route_link: RouteLink = parser.parse(element, RouteLink)
    print("1", route_link.id)

for element in tree.iterfind(".//{http://www.netex.org.uk/netex}RouteLink"):
    route_link: RouteLink = parser.parse(element, RouteLink)
    print("2", route_link.id)