from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

from netex import PublicationDelivery

def export_publication_delivery_xml(publication_delivery: PublicationDelivery, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True,encoding="utf-8")
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    if output_filename.endswith('.gz'):
        with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2 * 10 ** 8,
                                 encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)
    else:
        with open(output_filename, 'w', encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)