import sys

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

from netexio.database import Database
from netexio.dbaccess import get_single

with Database(sys.argv[1], read_only=True) as db_read:
    object = get_single(db_read, db_read.get_class_by_name(sys.argv[2]), sys.argv[3])
    serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    print(serializer.render(object, ns_map))
