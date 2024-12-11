import sys
from decimal import Decimal
from typing import List, Tuple

from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.datatype import XmlDateTime, XmlDuration, XmlTime
import random

from netexio.database import Database
from netexio.dbaccess import load_local, load_embedded, load_referencing, recursive_attributes, \
    load_referencing_inwards, resolve_all_references_and_embeddings, get_interesting_classes, recursive_resolve
import netex
from netex import ServiceJourney, VersionOfObjectRef, MultilingualString, ScheduledStopPointRef, \
    VersionOfObjectRefStructure, GeneralFrame, PublicationDelivery, ParticipantRef, DataObjectsRelStructure, \
    GeneralFrameMembersRelStructure, AvailabilityConditionRef, Route, ServiceJourneyPattern
import netex_monkeypatching
from aux_logging import *
import logging
import traceback

from transformers.embedding import embedding_update

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

def fetch(database: str, object_type: str, object_filter: str, output_filename: str):
    classes = get_interesting_classes()
    if object_type not in classes[0]:
        log_all(logging.WARN, 'related_explorer', f"no such object type found {object_type}")
        return

    filter_set = {Route, ServiceJourneyPattern}
    filter_set.add(getattr(sys.modules['netex'], object_type))

    with Database(database) as db:
        objs=[]
        if object_filter == "random":
            objs = load_local(db, getattr(netex, object_type))
            objs = [random.choice(objs)] # randomly select one
        else:
            objs = load_local(db, getattr(netex, object_type), filter=object_filter)

        if len(objs) > 0:
            obj = objs[0]

            resolved = []

            recursive_resolve(db, obj, resolved, obj.id, filter_set)

            publication_delivery = PublicationDelivery(
                version="ntx:1.1",
                publication_timestamp=XmlDateTime.now(),
                participant_ref=ParticipantRef(value="PyNeTExConv"),
                data_objects=DataObjectsRelStructure(choice=[
                    GeneralFrame(
                        id="Results", version="1",
                        members=GeneralFrameMembersRelStructure(choice=resolved))]))

            ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

            if output_filename.endswith('.gz'):
                with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2*10**8, encoding='utf-8') as out:
                    serializer.write(out, publication_delivery, ns_map)
            elif output_filename == '-':
                print(serializer.render(publication_delivery, ns_map))
            else:
                with open(output_filename, 'w', encoding='utf-8') as out:
                    serializer.write(out, publication_delivery, ns_map)
        else:
            log_all(logging.WARN, 'related_explorer',f"no such object found {object_type},{object_filter}")

def main(netex,object_type,object_filter,output,log_file,referencing):
    with Database(netex) as db:
        references_exist = False
        try:
            db.con.execute("SELECT * FROM referencing LIMIT 1;")
            db.con.execute("SELECT * FROM embedded LIMIT 1;")
            references_exist = True
        except:
            pass

        if referencing or not references_exist:
            log_all(logging.INFO, 'related_explorer',f"updating embedded and referencing tables")
            embedding_update(db)

    try:
        fetch(netex, object_type, object_filter, output)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e
if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Export a prepared EPIP  import into DuckDB')
    argument_parser.add_argument('netex', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('object_type', type=str, help='The NeTEx object type to filter, for example ServiceJourney')
    argument_parser.add_argument('object_filter', type=str, help='The object filter to apply.')
    argument_parser.add_argument('output', type=str, nargs="?", default="-", help='The NeTEx output filename, for example: netex.xml.gz')
    argument_parser.add_argument('--referencing', action="store_true", help='Create referencing table')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger = prepare_logger(logging.INFO,args.log_file)

    main(args.netex,args.object_type,args.object_filter,args.output,args.log_file,args.referencing)
