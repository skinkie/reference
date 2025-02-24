from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from memory_profiler import memory_usage

from netex import Codespace, AvailabilityCondition, NoticeAssignment, Notice, ScheduledStopPoint, \
    ServiceJourneyInterchange, Operator, ResponsibilitySet, StopPlace, Direction, Line, TariffZone, ServiceLink, \
    ServiceJourneyPattern, PassengerStopAssignment, DefaultConnection, SiteConnection, Connection, DataSource, \
    Authority, ValueSet, TransportAdministrativeZone, TopographicPlace, Network, DestinationDisplay, VehicleType, \
    ServiceJourney, DayType, DayTypeAssignment, UicOperatingPeriod
from netexio.database import Database
from netexio.dbaccess import setup_database, copy_table, missing_class_update
from netexio.pickleserializer import MyPickleSerializer
from transformers.interchanges import interchange_rules_to_service_journey_interchanges
from utils import get_interesting_classes
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
    epip_service_journey_generator, epip_service_journey_interchange, epip_interchange_rule, epip_service_calendar

from transformers.epip import EPIP_CLASSES
from aux_logging import *
from configuration import defaults

generator_defaults = {'codespace': Codespace(xmlns=defaults["codespace"]), 'version': defaults["version"]} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def main(source_database_file: str, target_database_file: str):
    classes = get_interesting_classes(filter=EPIP_CLASSES)

    with Database(target_database_file, serializer=MyPickleSerializer(compression=True), read_only=False) as target_db:
        setup_database(target_db, classes, True)
        # attach_source(con, source_database_file) does not work persistently, requires an attach at every connection

        with Database(source_database_file, MyPickleSerializer(compression=True), read_only=True) as source_db:
            log_all(logging.INFO, "Copy all tables as-is " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            copy_table(source_db, target_db,[Codespace, Direction, DataSource, Authority, Operator, ValueSet, TransportAdministrativeZone, VehicleType, ResponsibilitySet, TopographicPlace, Network, DestinationDisplay, ScheduledStopPoint], clean=True, embedding=True)
            source_db.clean_cache()

            log_all(logging.INFO, "Copy lines, in EPIP style " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_line_memory(source_db, target_db, generator_defaults)
            source_db.clean_cache()

            log_all(logging.INFO, "Fix Quay / StopPlace locations " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            infer_locations_from_quay_or_stopplace_and_apply(source_db, target_db, generator_defaults)
            source_db.clean_cache()
            # # epip_scheduled_stop_point_memory(target_db, target_db, generator_defaults)

            log_all(logging.INFO, "Investigate this site frame step " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_site_frame_memory(source_db, target_db, generator_defaults)
            source_db.clean_cache()

            log_all(logging.INFO, "Service journeys " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_service_journey_generator(source_db, target_db, generator_defaults, None, cache=False)
            source_db.clean_cache()

            log_all(logging.INFO, "Calendars " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_service_calendar(source_db, target_db, generator_defaults)
            source_db.clean_cache()

            log_all(logging.INFO, "ServiceJourneyInterchange additions " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_service_journey_interchange(source_db, target_db, generator_defaults)
            source_db.clean_cache()

            log_all(logging.INFO, "InterchangeRule additions " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            epip_interchange_rule(source_db, target_db, generator_defaults)
            source_db.clean_cache()

            log_all(logging.INFO, "Infer directions from ServiceJourneyPatterns, and apply " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            infer_directions_from_sjps_and_apply(target_db, target_db, generator_defaults)
            source_db.clean_cache()
            # TODO: epip_noticeassignment(source_db, target_db, generator_defaults)

            log_all(logging.INFO, "Reprojection Update " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            reprojection_update(target_db, 'urn:ogc:def:crs:EPSG::4326')

            log_all(logging.INFO, "Embedding update " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            embedding_update(target_db, filter_clazz=[Line, StopPlace, ServiceJourneyPattern, ServiceJourney, DayType, DayTypeAssignment, UicOperatingPeriod, ServiceJourneyInterchange, Direction])

            log_all(logging.INFO, "Copy remaining classes " + str(memory_usage(-1, interval=.1, timeout=1)[0]))
            missing_class_update(source_db, target_db)

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
        log_all(logging.ERROR, f'{e} {traceback.format_exc()}')
        raise e
