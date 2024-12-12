# This code is written to export all data into a NeTEx GeneralFrame this should be our complete database state
import sys
from typing import Generator

from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.datatype import XmlDateTime

from epip_db_to_xml import GeneratorTester
from netex import PublicationDelivery, ParticipantRef, DataObjectsRelStructure, GeneralFrame, \
    GeneralFrameMembersRelStructure, ScheduledStopPoint, Line
from netexio.database import Database
from netexio.dbaccess import load_generator

def chain(*iterables) -> Generator:
    for it in iterables:
        for element in it:
            yield element

def export_to_general_frame(db: Database, output_filename: str):
    iterables = [load_generator(db, getattr(sys.modules['netex'], table), embedding=False) for table in db.tables()]

    publication_delivery = PublicationDelivery(
        version="ntx:1.1",
        publication_timestamp=XmlDateTime.now(),
        participant_ref=ParticipantRef(value="PyNeTExConv"),
        data_objects=DataObjectsRelStructure(choice=[
            GeneralFrame(
                id="Database", version="1",
                members=GeneralFrameMembersRelStructure(choice=chain(*iterables)))]))

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

    if output_filename.endswith('.gz'):
        with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2 * 10 ** 8,
                                 encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)
    elif output_filename == '-':
        print(serializer.render(publication_delivery, ns_map))
    else:
        with open(output_filename, 'w', encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)
