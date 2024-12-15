from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import Codespace, AvailabilityCondition, NoticeAssignment, Notice, ScheduledStopPoint
from netexio.database import Database
from netexio.dbaccess import setup_database, copy_table, get_interesting_classes
from netexio.dbaccess import attach_source, attach_objects

from transformers.direction import infer_directions_from_sjps_and_apply
from transformers.embedding import embedding_update
from transformers.projection import reprojection_update
from transformers.scheduledstoppoint import infer_locations_from_quay_or_stopplace_and_apply
import traceback
context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

import netex_monkeypatching
from transformers.epip import epip_line_memory, epip_scheduled_stop_point_memory, epip_site_frame_memory, \
    epip_service_journey_generator

from transformers.epip import EPIP_CLASSES
from aux_logging import *

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def main(source_database_file: str, target_database_file: str):
    classes = get_interesting_classes(filter=EPIP_CLASSES)

    with Database(target_database_file, read_only=False) as target_db:
        setup_database(target_db, classes, True)
        # attach_source(con, source_database_file) does not work persistently, requires an attach at every connection

        with Database(source_database_file, read_only=True) as source_db:
            copy_table(source_db, target_db,[Notice, ScheduledStopPoint], clean=True)
            epip_line_memory(source_db, target_db, generator_defaults)
            infer_locations_from_quay_or_stopplace_and_apply(source_db, target_db, generator_defaults)
            # epip_scheduled_stop_point_memory(target_db, target_db, generator_defaults)
            epip_site_frame_memory(source_db, target_db, generator_defaults)
            epip_service_journey_generator(source_db, target_db, generator_defaults, None)
            infer_directions_from_sjps_and_apply(target_db, target_db, generator_defaults)

        reprojection_update(target_db, 'urn:ogc:def:crs:EPSG::4326')

        embedding_update(target_db)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Transform the input into mandatory objects for the export of EPIP')
    parser.add_argument('source', type=str, help='DuckDB file to use as input of the transformation.')
    parser.add_argument('target', type=str, help='DuckDB file to overwrite and store contents of the transformation.')
    parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = parser.parse_args()
    mylogger =prepare_logger(logging.INFO,args.log_file)
    try:
        main(args.source, args.target)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e
