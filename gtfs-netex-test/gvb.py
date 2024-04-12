from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import PublicationDelivery, PassengerCapacity
from netex import OnlineServiceOperatorVersionStructure

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

ns_map = {None: 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
pd = parser.parse(open('/tmp/gvb.xml', 'rb'), PublicationDelivery)
serializer.write(open('/tmp/new.xml', 'w'), pd, ns_map)

# OnlineServiceOperatorVersionStructure(address=OnlineServiceOperatorVersionStructure.Address())
