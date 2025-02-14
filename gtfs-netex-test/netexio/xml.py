from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
import zipfile
import io
from netex import PublicationDelivery

def export_publication_delivery_xml(publication_delivery: PublicationDelivery, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    if output_filename.endswith('.gz'):
        with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2 * 10 ** 8,
                                 encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)
    elif output_filename.endswith('.zip'):
        # Create an in-memory text stream
        xml_buffer = io.StringIO()
        serializer.write(xml_buffer, publication_delivery, ns_map)

        # Get the XML content as a string
        xml_content = xml_buffer.getvalue()

        # Write the XML content to a zip file
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Use a BytesIO buffer to write the string as bytes
            with io.BytesIO(xml_content.encode('utf-8')) as xml_bytes:
                zipf.writestr('publication_delivery.xml', xml_bytes.read())
    else:
        with open(output_filename, 'w', encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)