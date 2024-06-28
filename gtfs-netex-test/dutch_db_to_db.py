import sys
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
from transformers.dutch import dutch_scheduled_stop_point_generator, \
    dutch_service_journey_pattern_time_demand_type_memory
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
    epip_service_journey_generator

from dutch_to_db import DUTCH_CLASSES

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1, 'DefaultLocationsystem': 'EPSG:28992'} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def main(source_database_file: str, target_database_file: str):
    classes = get_interesting_classes(filter=DUTCH_CLASSES)
    with sqlite3.connect(target_database_file) as con:
        setup_database(con, classes, True)


        with Pool(1) as pool:
            # dutch_scheduled_stop_point_generator(source_database_file, target_database_file, generator_defaults, pool)
            dutch_service_journey_pattern_time_demand_type_memory(source_database_file, target_database_file, generator_defaults)

    # Add a single responsibility set and TransportAdministrativeZone
    # Infer OperationalContext from Line (Transportmode)
    # Add a fake VehicleType
    # Create routePoints, routeLinks, Routes
    # Create DestinationDisplays (from DestinationDisplayViews)
    # Create StopArea
    # Create StopAssignments
    # Create TimingLinks
    # Create ServiceJourneyPatterns
    # Create TimeDemandType
    # Create AvailabilityCondition
    # OperatorView/OperatorRef




    # epip_line_memory(source_database_file, target_database_file, generator_defaults)
    # epip_scheduled_stop_point_memory(source_database_file, target_database_file, generator_defaults)
    # epip_site_frame_memory(source_database_file, target_database_file, generator_defaults)
    # epip_service_journey_generator(source_database_file, target_database_file, generator_defaults, None)
    # infer_directions_from_sjps_and_apply(target_database_file, target_database_file, generator_defaults)

    # epip_service_journey_generator(source_database_file, target_database_file, generator_defaults, None)


if __name__ == '__main__':
    main("/home/netex/delijn-netex.duckdb", "/home/netex/delijn-nl.duckdb")
