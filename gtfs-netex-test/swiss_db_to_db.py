import sqlite3
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
from netexio.dbaccess import load_generator
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

SOURCE_DATABASE_FILE = "/home/netex/swiss.sqlite"
TARGET_DATABASE_FILE = "/home/netex/swiss-target.sqlite"

def main():
    # classes = get_interesting_classes(filter=EPIP_CLASSES)
    # with sqlite3.connect(TARGET_DATABASE_FILE) as con:
        # setup_database(con, classes, True)
        # epip_line_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
        # epip_scheduled_stop_point_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
        # epip_site_frame_memory(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)

    # with Pool(1) as pool:
    #    epip_service_journey_generator(SOURCE_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults, pool)


    # infer_directions_from_sjps_and_apply(TARGET_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)
    # epip_remove_keylist_extensions(TARGET_DATABASE_FILE, TARGET_DATABASE_FILE, generator_defaults)


    # with Pool(10) as pool:
        # kwargs = {'read_database': "/home/netex/netex.sqlite", 'write_database': "/home/netex/target.sqlite", 'generator_defaults': generator_defaults}
    #bison_codespaces("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)
        # epip_line_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
    #epip_line_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

    #epip_route_point_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

    #epip_route_link_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

    #epip_scheduled_stop_point_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)
        # epip_scheduled_stop_point_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

        # epip_scheduled_stop_point("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
        # epip_scheduled_stop_point2("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
        # epip_scheduled_stop_point3("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

        # epip_route_point_memory(**kwargs)
        # epip_route_link_memory(**kwargs)


    # line_ref_by_sjp = line_ref_from_route("/home/netex/netex.sqlite")
    # epip_timetabled_passing_times_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

    # epip_service_journey_patterns("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)


    # epip_timetabled_passing_times_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
        # epip_timetabled_passing_times_generator2("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

        # pool.starmap(wrapper, [(bison_codespaces, kwargs),
        #                        (epip_site_frame, kwargs),
        #                        (epip_route_point, kwargs),
        #                        (epip_route_link, kwargs),
        #                        (epip_scheduled_stop_point, kwargs),
        #                        (epip_timetabled_passing_times, kwargs),
        #                        (epip_service_journey_patterns, kwargs),
        #                        ])



    # Voor alle PointsInJourneyPattern, als TimingLink een ServiceLink zou kunnen zijn, haal op basis van PointProjection de RouteLink op waar deze informatie
    # in zou kunnen zitten. Doe dit niet exclusief op basis van From/To maar neem de Route die in het ServiceJourneyPattern staat mee als referentie.
    # In het geval dat er sprake is van een TimingPointInJourneyPattern, haal dan de route op tot de eerst volgende ScheduledStopPoint en voeg de verschillende
    # RouteLinks samen, houdt er rekening mee dat bij het samen voegen het laatste punt op de lijn gelijk is aan het eerste, en daarmee overgeslagen zou
    # moeten worden.

    # TODO: In EPIP noticeAssignments should be embedded in the object, and not separate.

    # TODO: Swiss NoticeAssignments on Call level now end up at StopPointInJourneyPattern.
    # They might be there at the correct location, but I guess they should be at TimetabledPassingTime.


if __name__ == '__main__':
    main()
