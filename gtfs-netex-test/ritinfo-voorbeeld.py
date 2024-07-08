from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from ritinfo import TreinRitType
import lxml

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

tree = lxml.etree.parse('/tmp/berichtje2.xml')
for element in tree.iterfind(".//{urn:ndov:cdm:trein:reisinformatie:data:2}RitInfo"):
    trein_rit: TreinRitType = parser.parse(element, TreinRitType)
    print(trein_rit)