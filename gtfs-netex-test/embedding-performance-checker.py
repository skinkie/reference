from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from netex import StopPlace
from netexio.dbaccess import update_embedded_referencing
from netexio.pickleserializer import MyPickleSerializer
import timeit

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
sp = parser.parse(Path("stopplace.xml"), StopPlace)

serializer = MyPickleSerializer()

# print(len(list(update_embedded_referencing(serializer, sp))))

print(timeit.timeit(lambda: list(update_embedded_referencing(serializer, sp)), number=500))

