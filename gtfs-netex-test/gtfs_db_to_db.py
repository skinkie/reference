import duckdb as sqlite3
from decimal import Decimal, ROUND_HALF_UP
from functools import partial
from itertools import chain
from typing import List, Iterable, T, Generator

from pyproj import Transformer, CRS
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from anyintodbnew import setup_database, get_interesting_classes
from callsprofile import CallsProfile
from dbaccess import load_generator
from netex import ServiceJourneyPattern, Direction, Codespace, MultilingualString, DirectionType, ServiceJourney, \
    AvailabilityCondition, TimeDemandType, ScheduledStopPoint, Pos, PointVersionStructure, RoutePoint, RouteLink, \
    StopPointInJourneyPattern, TimingPointInJourneyPattern, ScheduledStopPointRef, TimingLink, ServiceLink, \
    TimingLinkRefStructure, ServiceLinkRefStructure, RouteRef, Route, RouteLinkRef, RouteLinkRefStructure, \
    RouteRefStructure, ScheduledStopPointRefStructure, RoutePointRef, RoutePointRefStructure, PointProjection, \
    TimingPoint, TimingPointRefStructure, LineString, Link, LinkVersionStructure, PosList, Line, StopPlace, AccessSpace, \
    Quay, Polygon, PassengerStopAssignment, QuayRefStructure, StopPlaceRefStructure, Block, ServiceJourneyRef, \
    VehicleTypeRef, VersionOfObjectRefStructure, ServiceJourneyPatternRef, LineRef

from refs import getId, getRef, getIndex
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from transformers.direction import infer_directions_from_sjps_and_apply
from transformers.site_frame import infer_stop_places
from utils import project
from multiprocess import Pool

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
    epip_service_journey_generator, epip_remove_keylist_extensions
from transformers.epip import EPIP_CLASSES

from swiss_to_db import SWISS_CLASSES

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1, 'DefaultLocationsystem': 'EPSG:4326'} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

SOURCE_DATABASE_FILE = "/home/netex/gtfs-source.duckdb"
TARGET_DATABASE_FILE = "/home/netex/gtfs-target.duckdb"

def main():
    classes = get_interesting_classes(filter=EPIP_CLASSES)
    with sqlite3.connect(TARGET_DATABASE_FILE) as con:
        setup_database(con, classes, True)
    epip_line_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
    epip_scheduled_stop_point_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
    epip_site_frame_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
    epip_service_journey_generator(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults, None)
    infer_directions_from_sjps_and_apply(TARGET_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)

if __name__ == '__main__':
    main()
