from decimal import Decimal
from typing import List, Tuple

from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.datatype import XmlDateTime, XmlDuration, XmlTime

from dbaccess import load_local
import netex
from netex import ServiceJourney, VersionOfObjectRef, MultilingualString, ScheduledStopPointRef, \
    VersionOfObjectRefStructure, GeneralFrame, PublicationDelivery, ParticipantRef, DataObjectsRelStructure, \
    GeneralFrameMembersRelStructure, AvailabilityConditionRef
import duckdb as sqlite3
from mro_attributes import list_attributes
import xsdata

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

def recursive_attributes(obj):
    for k, v in obj.__dict__.items():
        if v is not None:
            # print(v)
            if issubclass(v.__class__, VersionOfObjectRef) or issubclass(v.__class__, VersionOfObjectRefStructure):
                yield v

            else:
                if (v.__class__.__name__ in netex.__all__ and hasattr(v, '__dict__')):
                    yield from recursive_attributes(v)
                elif v.__class__ in (list, tuple):
                    for x in v:
                        if issubclass(x.__class__, VersionOfObjectRef) or issubclass(x.__class__,
                                                                                     VersionOfObjectRefStructure):
                            yield x
                        else:
                            yield from recursive_attributes(x)


def recursive_resolve(con, parent, resolved):
    resolved.append(parent)

    for obj in recursive_attributes(parent):
        if obj.name_of_ref_class is None:
            # Hack, because NeTEx does not define the default name of ref class yet
            obj.name_of_ref_class = obj.__class__.__name__[0:-3]

        if obj in resolved:
            continue

        resolved_objs = load_local(con, getattr(netex, obj.name_of_ref_class), filter=obj.ref)
        if len(resolved_objs) > 0:
            recursive_resolve(con, resolved_objs[0], resolved)

def fetch(database: str, object_type: str, object_filter: str, output_filename: str):
    with sqlite3.connect(database) as con:
        objs = load_local(con, getattr(netex, object_type), filter=object_filter)
        if len(objs) > 0:
            obj = objs[0]

            resolved = []
            recursive_resolve(con, obj, resolved)

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

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Export a prepared EPIP  import into DuckDB')
    argument_parser.add_argument('netex', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('object_type', type=str, help='The NeTEx object type to filter, for example ServiceJourney')
    argument_parser.add_argument('object_filter', type=str, help='The object filter to apply.')
    argument_parser.add_argument('output', type=str, nargs="?", default="-", help='The NeTEx output filename, for example: netex.xml.gz')
    args = argument_parser.parse_args()

    fetch(args.netex, args.object_type, args.object_filter, args.output)