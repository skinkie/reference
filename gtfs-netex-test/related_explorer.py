import sys
from decimal import Decimal
from typing import List, Tuple

from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.datatype import XmlDateTime, XmlDuration, XmlTime
import random


from netexio.dbaccess import load_local, load_embedded, load_referencing, recursive_attributes, \
    load_referencing_inwards, resolve_all_references_and_embeddings, get_interesting_classes
import netex
from netex import ServiceJourney, VersionOfObjectRef, MultilingualString, ScheduledStopPointRef, \
    VersionOfObjectRefStructure, GeneralFrame, PublicationDelivery, ParticipantRef, DataObjectsRelStructure, \
    GeneralFrameMembersRelStructure, AvailabilityConditionRef, Route, ServiceJourneyPattern
import netex_monkeypatching
import duckdb as sqlite3
from mro_attributes import list_attributes
import xsdata
from aux_logging import *
import logging
import traceback
serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)



def recursive_resolve(con, parent, resolved, filter=None, filter_class=set([])):
    for x in resolved:
        if parent.id == x.id and parent.__class__ == x.__class__:
            return

    resolved.append(parent)

    if filter is False or filter == parent.id or parent.__class__ in filter_class:
        resolved_parents = load_referencing_inwards(con, parent.__class__, filter=parent.id)
        if len(resolved_parents) > 0:
            for y in resolved_parents:
                already_done = False
                for x in resolved:
                    if y[0] == x.id and getattr(sys.modules['netex'], y[2]) == x.__class__:
                        already_done = True
                        break
    
                if not already_done:
                    resolved_objs = load_local(con, getattr(sys.modules['netex'], y[2]),
                                               filter=y[0], embedding=False)
                    if len(resolved_objs) > 0:
                        recursive_resolve(con, resolved_objs[0], resolved, filter, filter_class)  # TODO: not only consider the first

    # In principle this would already take care of everything recursive_attributes could find, but now does it inwards.
    resolved_parents = load_referencing(con, parent.__class__, filter=parent.id)
    if len(resolved_parents) > 0:
        for y in resolved_parents:
            already_done = False
            for x in resolved:
                if y[0] == x.id and getattr(sys.modules['netex'], y[2]) == x.__class__:
                    already_done = True
                    break

            if not already_done:
                resolved_objs = load_local(con, getattr(sys.modules['netex'], y[2]),
                                           filter=y[0], embedding=False)
                if len(resolved_objs) > 0:
                    recursive_resolve(con, resolved_objs[0], resolved, filter, filter_class)  # TODO: not only consider the first
    # else:
    #      print(f"Cannot resolve referencing {parent.id}")

    for obj in recursive_attributes(parent):
        if hasattr(obj, 'id'):
            continue

        elif hasattr(obj, 'name_of_ref_class'):
            if obj.name_of_ref_class is None:
                # Hack, because NeTEx does not define the default name of ref class yet
                if obj.__class__.__name__.endswith('RefStructure'):
                    obj.name_of_ref_class = obj.__class__.__name__[0:-12]
                elif obj.__class__.__name__.endswith('Ref'):
                    obj.name_of_ref_class = obj.__class__.__name__[0:-3]

            if not hasattr(netex, obj.name_of_ref_class):
                #hack for non-existing structures
                print(f'No attribute found in module {netex} for {obj.name_of_ref_class}.')
                continue

            clazz = getattr(netex, obj.name_of_ref_class)

            # TODO: do this via a hash function
            # if obj in resolved:
            #    continue
            already_done = False
            for x in resolved:
                if obj.ref == x.id and clazz == x.__class__:
                    already_done = True
                    break

            if not already_done:
                resolved_objs = load_local(con, clazz, filter=obj.ref, embedding=False)
                if len(resolved_objs) > 0:
                    recursive_resolve(con, resolved_objs[0], resolved, filter, filter_class) # TODO: not only consider the first
                else:
                    # print(obj.ref)
                    resolved_parents = load_embedded(con, clazz, filter=obj.ref)
                    if len(resolved_parents) > 0:
                        for y in resolved_parents:
                            already_done = False
                            for x in resolved:
                                if y[0] == x.id and getattr(sys.modules['netex'], y[2]) == x.__class__:
                                    already_done = True
                                    break

                            if not already_done:
                                resolved_objs = load_local(con, getattr(sys.modules['netex'], y[2]), filter=y[0], embedding=False)
                                if len(resolved_objs) > 0:
                                    recursive_resolve(con, resolved_objs[0], resolved, filter, filter_class) # TODO: not only consider the first
                    else:
                        print(f"Cannot resolve embedded {obj.ref}")

def fetch(database: str, object_type: str, object_filter: str, output_filename: str):
    with sqlite3.connect(database) as con:
        try:
            con.execute("SELECT * FROM referencing LIMIT 1;")
            con.execute("SELECT * FROM embedded LIMIT 1;")
        except:
            pass
            classes = get_interesting_classes()
            resolve_all_references_and_embeddings(con, classes)


        objs=[]
        if object_filter == "random":
            objs = load_local(con, getattr(netex, object_type))
            objs = [random.choice(objs)] #randomly select one
        else:
            objs = load_local(con, getattr(netex, object_type), filter=object_filter)
        if len(objs) > 0:
            obj = objs[0]

            resolved = []
            recursive_resolve(con, obj, resolved, obj.id, {Route, ServiceJourneyPattern})

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
            print(f"no such object found {object_type},{object_filter}")
if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Export a prepared EPIP  import into DuckDB')
    argument_parser.add_argument('netex', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('object_type', type=str, help='The NeTEx object type to filter, for example ServiceJourney')
    argument_parser.add_argument('object_filter', type=str, help='The object filter to apply.')
    argument_parser.add_argument('output', type=str, nargs="?", default="-", help='The NeTEx output filename, for example: netex.xml.gz')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)
    try:
        fetch(args.netex, args.object_type, args.object_filter, args.output)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e

