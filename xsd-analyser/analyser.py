import inspect

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import lxml
import netex
from xsd import Keyref

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

tree = lxml.etree.parse("/home/skinkie/Sources/NeTEx/xsd/NeTEx_publication.xsd")

result = set([])
for selector in tree.iterfind(".//{http://www.w3.org/2001/XMLSchema}selector"):
    selector: Keyref
    xpaths = [x.strip() for x in selector.attrib['xpath'].split('|')]
    for xpath in xpaths:
        xpath = xpath.split('/')[0].split('netex:')[-1]
        result.add(xpath)

netex_classes = set([])
for name, obj in inspect.getmembers(netex):
    if inspect.isclass(obj):
        if hasattr(obj, 'Meta') and hasattr(obj.Meta, 'name'):
            name = obj.Meta.name
        netex_classes.add(name)

available = result - netex_classes
print(available)

