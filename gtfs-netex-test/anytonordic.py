# Nordic Profile
#
# @version is an integer
#
# shared.xml
#
# ResourceFrame
# -> DataSources
# -> Organisations
#
# ServiceFrame
# -> Network
# -> RoutePoints
# -> DestinationDiplays
# -> ScheduledStopPoints
# -> TimingLinks
# -> ServiceLinks
# -> StopAssignments
#
# ServiceCalendarFrame
# -> DayTypes
# -> DayTypeAssignments
#
# line.xml
#
# ResourceFrame
# -> DataSources (for Sweden)
#
# ServiceFrame
# -> Routes
# -> Lines
# -> JourneyPattern
#
# TimetableFrame
# -> vehicleJourneys
from typing import List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
import lxml

from cleanupprofile import CleanupProfile
from netex import AvailabilityCondition, ServiceJourney, ServiceJourneyPattern, Codespace, Version, \
    ServiceCalendarFrame, TypeOfFrameRef, Line, DeadRunJourneyPattern, JourneyPattern, Route, Operator, \
    PublicationDelivery, Network, GroupsOfLinesInFrameRelStructure, RoutePoint, DestinationDisplay, ScheduledStopPoint, \
    TimingPoint, ServiceLink, TimingLink, PassengerStopAssignment, DayType, DayTypeAssignment, OperatingPeriod, \
    UicOperatingPeriod
from nordicprofile import NordicProfile
from refs import getId, getIndex
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}


nsr = {"Flix:ScheduledStopPoint:191c1ce4-c9e3-4f33-a131-53e595ac4a26": ('NSR:StopPlace:57993', 'NSR:Quay:99384'),
        "Flix:ScheduledStopPoint:3a60555c-ef49-4287-bef1-e9d69314d8db": ('NSR:StopPlace:57997', 'NSR:Quay:99388'),
       "Flix:ScheduledStopPoint:77b1e6b1-df82-4ca0-96c5-6fb737df4317": ('', 'NSR:Quay:99383'),
       "Flix:ScheduledStopPoint:cbb7c38b-29b4-40ea-ae49-3c9e7ef04fe7": ('', 'NSR:Quay:99385'),
        "Flix:ScheduledStopPoint:dcc03476-9603-11e6-9066-549f350fcb0c": ('', 'NSR:Quay:99386'),
       "Flix:ScheduledStopPoint:dcc38945-9603-11e6-9066-549f350fcb0c": ('', 'NSR:Quay:11974'),
       "Flix:ScheduledStopPoint:dd5e6677-34c6-4be2-86c6-3fbdfb6ec5e7": ('', 'NSR:Quay:99387'),
        "Flix:ScheduledStopPoint:eb6950c9-97bd-4486-bdf2-ca7401b0c911": ('NSR:StopPlace:58188', 'NSR:Quay:102058'),
        "Flix:ScheduledStopPoint:f15a36ff-6dc9-4ea2-919d-2f2cb1b5ba44": ('NSR:StopPlace:57991', 'NSR:Quay:99382')
}

def conversion(input_filename: str, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    service_journeys = []
    journey_patterns = []
    availability_conditions = []
    operators = []
    lines = []
    routes = []
    networks = []
    route_points = []
    destination_displays = []
    scheduled_stop_points = []
    timing_points = []
    timing_links = []
    service_links = []
    stop_assignments = []
    day_types = []
    day_type_assignments = []
    operating_periods = []

    tree = lxml.etree.parse(input_filename)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Network"):
        network: Network = parser.parse(element, Network)
        networks.append(network)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}RoutePoint"):
        route_point: RoutePoint = parser.parse(element, RoutePoint)
        route_points.append(route_point)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DestinationDisplay"):
        destination_display: DestinationDisplay = parser.parse(element, DestinationDisplay)
        destination_displays.append(destination_display)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
        scheduled_stop_point: ScheduledStopPoint = parser.parse(element, ScheduledStopPoint)
        scheduled_stop_points.append(scheduled_stop_point)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}TimingPoint"):
        timing_point: TimingPoint = parser.parse(element, TimingPoint)
        timing_points.append(timing_point)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}TimingLink"):
        timing_link: TimingLink = parser.parse(element, TimingLink)
        timing_links.append(timing_link)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceLink"):
        service_link: ServiceLink = parser.parse(element, ServiceLink)
        service_links.append(service_link)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}PassengerStopAssignment"):
        passenger_stop_assignment: PassengerStopAssignment = parser.parse(element, PassengerStopAssignment)
        ssp = passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point
        if ssp.ref in nsr:
            passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place = nsr[ssp.ref][0]
            passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place = None
            passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref = nsr[ssp.ref][1]
            passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.version = None
        stop_assignments.append(passenger_stop_assignment)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayType"):
        day_type: DayType = parser.parse(element, DayType)
        day_types.append(day_type)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayTypeAssignment"):
        day_type_assignment: DayTypeAssignment = parser.parse(element, DayTypeAssignment)
        day_type_assignments.append(day_type_assignment)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}OperatingPeriod"):
        operating_period: OperatingPeriod = parser.parse(element, OperatingPeriod)
        operating_periods.append(operating_period)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}UicOperatingPeriod"):
        uic_operating_period: UicOperatingPeriod = parser.parse(element, UicOperatingPeriod)
        operating_periods.append(uic_operating_period)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Operator"):
        operator: Operator = parser.parse(element, Operator)
        operators.append(operator)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
        line: Line = parser.parse(element, Line)
        NordicProfile.changeRemoveBackgroundColour(line)
        lines.append(line)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}contentValidityConditions/{http://www.netex.org.uk/netex}AvailabilityCondition"):
        availability_condition: AvailabilityCondition = parser.parse(element, AvailabilityCondition)
        availability_conditions.append(availability_condition)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
        service_journey: ServiceJourney = parser.parse(element, ServiceJourney)
        service_journeys.append(service_journey)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Route"):
        route: Route = parser.parse(element, Route)
        routes.append(route)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourneyPattern"):
        service_journey_pattern: ServiceJourneyPattern = parser.parse(element, ServiceJourneyPattern)
        journey_patterns.append(service_journey_pattern)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DeadRunJourneyPattern"):
        dead_run_journey_pattern: DeadRunJourneyPattern = parser.parse(element, DeadRunJourneyPattern)
        journey_patterns.append(dead_run_journey_pattern)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}JourneyPattern"):
        journey_pattern: JourneyPattern = parser.parse(element, JourneyPattern)
        journey_patterns.append(journey_pattern)

    if len(service_journeys) == 0:
        return

    codespace = Codespace(id="OPENOV", xmlns="OPENOV", xmlns_url="http://openov.nl/")
    version = Version(id="OPENOV:Version:1", version="1")

    # servicecalendarepip = ServiceCalendarEPIPFrame(codespace)
    # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    # service_calendar_frame = ServiceCalendarFrame(id=getId(ServiceCalendarFrame, codespace, "ServiceCalendarFrame"), version="1",
                                                  # type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"),
    #                                              service_calendar=service_calendar)

    # timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys, service_journey_patterns)
    # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

    profile = NordicProfile(Codespace(id="OPENOV", xmlns="OPENOV"), None, Version(version="1"))

    for journey_pattern in journey_patterns:
        CleanupProfile.firstAndLastStop(journey_pattern)

    for line in lines:
        these_service_journeys = [service_journey for service_journey in service_journeys if service_journey.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view.ref == line.id]
        # timetabledpassingtimesprofile = TimetablePassingTimesProfile(self.codespace, self.version, service_journeys, service_journey_patterns)
        # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

        if len(these_service_journeys) > 0:
            timetable_frame = profile.getTimetableFrame(line, these_service_journeys, journey_patterns)
            these_journey_patterns = [y for y in journey_patterns if y.id in [x.journey_pattern_ref.ref for x in these_service_journeys]]
            these_routes = [y for y in routes if y.id in [x.route_ref_or_route_view.ref for x in these_journey_patterns]]

            service_frame = profile.getServiceFrame(line, these_journey_patterns, these_routes)
            publication_delivery: PublicationDelivery = profile.getLineDelivery(line, [], [service_frame], [timetable_frame])

            filename: str = f'netex-output-nordic/{line.id.replace(":", "_").replace("/", "_")}.xml'
            with open(filename, 'w') as out:
                serializer.write(out, publication_delivery, ns_map)

            NordicProfile.changeCodeSpaceNaive(filename, "ENT")
            NordicProfile.changeRemoveVersion(filename)


    resource_frame = profile.getResourceFrameShared(operators)
    if len(networks) == 0:
        network = profile.projectNetworkFromLines(lines)
    else:
        network = networks[0]


    service_frame = profile.getServiceFrameShared(network, route_points, [], routes, destination_displays, scheduled_stop_points, timing_points, timing_links, service_links, stop_assignments)

    operating_periods_index = getIndex(operating_periods)
    day_type_assignments_date: List[DayTypeAssignment] = []
    for day_type_assignment in day_type_assignments:
        day_type_assignments_date += NordicProfile.projectDayTypeAssignmentToDayTypeAssignmentDate(day_type_assignment, operating_periods=operating_periods_index)

    service_calendar_frame = profile.getServiceCalendarFrameShared(day_types, day_type_assignments_date)

    publication_delivery: PublicationDelivery = profile.getShared([resource_frame], [service_frame], [service_calendar_frame])
    with open(f'netex-output-nordic/shared.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)
    NordicProfile.changeCodeSpaceNaive('netex-output-nordic/shared.xml', "ENT")


conversion("netex-output-epip/Flix_Line_N600.xml", "")