import datetime
from io import BytesIO
from typing import Iterator, Type, T, Optional
import duckdb
import pandas
from duckdb.duckdb import DuckDBPyConnection
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDate

from netex import ServiceFrame, ScheduledStopPointsInFrameRelStructure, ScheduledStopPoint, LinesInFrameRelStructure, \
    Line, JourneyPatternsInFrameRelStructure, ServiceJourneyPattern, DeadRun, DeadRunJourneyPattern, TimetableFrame, \
    JourneysInFrameRelStructure, CompositeFrame, TypeOfFrameRef, FramesRelStructure, PublicationDelivery, \
    DataObjectsRelStructure, ServiceCalendarFrame, ServiceCalendar, DayTypesRelStructure, DayType, \
    OperatingPeriodsRelStructure, DayTypeAssignmentsRelStructure, UicOperatingPeriod, DayTypeAssignment, SiteFrame, \
    StopPlacesInFrameRelStructure, StopPlace, StopAssignmentsInFrameRelStructure, ResourceFrame, \
    DataSourcesInFrameRelStructure, DataSource, OrganisationsInFrameRelStructure, CodespacesRelStructure, Codespace, \
    VersionFrameDefaultsStructure, ParticipantRef

ns_map = {None: 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

con = duckdb.connect(database='merge.duckdb')
class generate_from_duckdb(list):
    def __init__(self, con: DuckDBPyConnection, query: str, type: Optional[Type[T]] = None, size=1000):
        super().__init__()
        self.con = con
        self.query = query
        self.type = type
        self.size = size

    def __iter__(self) -> Iterator:
        cur = duckdb.cursor(self.con)
        cur.execute(self.query)
        while True:
            results = cur.fetchmany(self.size)
            if not results:
                break
            for result in results:
                yield parser.parse(lxml.etree.fromstring(result[0]), self.type)


serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

QUERY_JP = """SELECT xml FROM journeyPatterns;"""
QUERY_LINE = """SELECT xml FROM lines;"""
QUERY_SSP = """SELECT xml FROM scheduledStopPoints;"""
QUERY_VJ = """SELECT xml FROM vehicleJourneys;"""
QUERY_DT = """SELECT xml FROM dayTypes;"""
QUERY_UOP = """SELECT xml FROM operatingPeriods;"""
QUERY_DTA = """SELECT xml FROM dayTypeAssignments;"""
QUERY_SP = """SELECT xml FROM stopPlaces;"""
QUERY_SA = """SELECT xml FROM stopAssignments;"""
QUERY_DS = """SELECT xml FROM dataSources;"""
QUERY_ORG = """SELECT xml FROM organisations;"""
QUERY_CS = """SELECT xml FROM codespaces;"""
QUERY_FD = """SELECT xml FROM FrameDefaults LIMIT 1;"""

with (open('/tmp/test.xml', 'w') as f):
    resource_frame = ResourceFrame(id="OPENOV:ResourceFrame:Aggregated", version="1",
                                   type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_COMMON", version_ref="epip:1.0"),
                                   data_sources=DataSourcesInFrameRelStructure(
                                       data_source=generate_from_duckdb(con, QUERY_DS, DataSource)),
                                   organisations=OrganisationsInFrameRelStructure(
                                       organisation_or_transport_organisation=generate_from_duckdb(con, QUERY_ORG)))

    service_frame = ServiceFrame(id="OPENOV:ServiceFrameFrame:Aggregated", version="1",
                                 type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_NETWORK", version_ref="epip:1.0"),
                                 journey_patterns=JourneyPatternsInFrameRelStructure(
                                     journey_pattern=generate_from_duckdb(con, QUERY_JP, ServiceJourneyPattern)
                                 ),
                                 lines=LinesInFrameRelStructure(
                                     line=generate_from_duckdb(con, QUERY_LINE, Line)),
                                 stop_assignments=StopAssignmentsInFrameRelStructure(
                                     stop_assignment=generate_from_duckdb(con, QUERY_SA)),
                                 scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                     scheduled_stop_point=generate_from_duckdb(con, QUERY_SSP, ScheduledStopPoint)))

    timetable_frame = TimetableFrame(id="OPENOV:TimetableFrame:Aggregated", version="1",
                                     type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_TIMETABLE", version_ref="epip:1.0"),
                                     vehicle_journeys=JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=generate_from_duckdb(con, QUERY_VJ))
                                     )

    from_dates = []
    to_dates = []
    x: UicOperatingPeriod
    for x in generate_from_duckdb(con, QUERY_UOP, UicOperatingPeriod):
        from_dates.append(x.from_operating_day_ref_or_from_date.to_datetime())
        to_dates.append(x.to_operating_day_ref_or_to_date.to_datetime())
    from_date = XmlDate.from_date(min(from_dates).date())
    to_date = XmlDate.from_date(max(to_dates).date())
    from_dates = None
    to_dates = None

    service_calendar_frame = ServiceCalendarFrame(id="OPENOV:ServiceCalendarFrame:Aggregated", version="1",
                                                  type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"),
                                                  service_calendar=ServiceCalendar(id="1",
                                                                                   version="1",
                                                                                   from_date=from_date,
                                                                                   to_date=to_date,
                                                                                   day_types=DayTypesRelStructure(day_type_ref_or_day_type=generate_from_duckdb(con, QUERY_DT, DayType)),
                                                                                   operating_periods=OperatingPeriodsRelStructure(uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period=generate_from_duckdb(con, QUERY_UOP, UicOperatingPeriod)),
                                                                                   day_type_assignments=DayTypeAssignmentsRelStructure(day_type_assignment=generate_from_duckdb(con, QUERY_DTA, DayTypeAssignment))))

    site_frame = SiteFrame(id="OPENOV:SiteFrame:Aggregated", version="1",
                           stop_places=StopPlacesInFrameRelStructure(stop_place=generate_from_duckdb(con, QUERY_SP, StopPlace)))

    composite_frame = CompositeFrame(id="OPENOV:CompositeFrame:Aggregated", version="1",
                                     type_of_frame_ref = TypeOfFrameRef(ref="EPIP:EU_PI_NETWORK_OFFER", version_ref="epip:1.0"),
                                     codespaces=CodespacesRelStructure(codespace_ref_or_codespace=generate_from_duckdb(con, QUERY_CS, Codespace)),
                                     frame_defaults=list(generate_from_duckdb(con, QUERY_FD, VersionFrameDefaultsStructure))[0]
                                     )
    composite_frame.frames = FramesRelStructure(common_frame=[resource_frame, service_frame, timetable_frame, service_calendar_frame, site_frame])

    publication_delivery = PublicationDelivery(participant_ref=ParticipantRef(value="PyNeTExConv"),
        publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()))
    publication_delivery.version = "ntx:1.1"
    publication_delivery.description = "NeTEx export"
    publication_delivery.data_objects = DataObjectsRelStructure(choice=[composite_frame])

    serializer.write(f, publication_delivery, ns_map)
