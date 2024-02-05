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
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
import lxml

from netex import AvailabilityCondition, ServiceJourney, ServiceJourneyPattern, Codespace, Version, \
    ServiceCalendarFrame, TypeOfFrameRef, Line, DeadRunJourneyPattern, JourneyPattern, Route, Operator, \
    PublicationDelivery, Network, GroupsOfLinesInFrameRelStructure, RoutePoint, DestinationDisplay, ScheduledStopPoint, \
    TimingPoint, ServiceLink, TimingLink, PassengerStopAssignment, DayType, DayTypeAssignment
from nordicprofile import NordicProfile
from refs import getId
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

def conversion(input_filename: str, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(serializer_config)

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
        stop_assignments.append(passenger_stop_assignment)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayType"):
        day_type: DayType = parser.parse(element, DayType)
        day_types.append(day_type)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayTypeAssignment"):
        day_type_assignment: DayTypeAssignment = parser.parse(element, DayTypeAssignment)
        day_type_assignments.append(day_type_assignment)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Operator"):
        operator: Operator = parser.parse(element, Operator)
        operators.append(operator)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
        line: Line = parser.parse(element, Line)
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

    profile = NordicProfile(None, None, Version(version="1"))

    for line in lines:
        these_service_journeys = [service_journey for service_journey in service_journeys if service_journey.choice.ref == line.id]
        # timetabledpassingtimesprofile = TimetablePassingTimesProfile(self.codespace, self.version, service_journeys, service_journey_patterns)
        # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

        if len(these_service_journeys) > 0:
            timetable_frame = profile.getTimetableFrame(line, these_service_journeys, journey_patterns)
            these_journey_patterns = [y for y in journey_patterns if y.id in [x.journey_pattern_ref.ref for x in these_service_journeys]]
            these_routes = [y for y in routes if y.id in [x.route_ref_or_route_view.ref for x in these_journey_patterns]]

            service_frame = profile.getServiceFrame(line, these_journey_patterns, these_routes)
            publication_delivery: PublicationDelivery = profile.getLineDelivery(line, [], [service_frame], [timetable_frame])

            with open(f'netex-output-nordic/{line.id.replace(":", "_").replace("/", "_")}.xml', 'w') as out:
                serializer.write(out, publication_delivery, ns_map)


    resource_frame = profile.getResourceFrameShared(operators)
    if len(networks) == 0:
        network = NordicProfile.projectNetworkFromLines(lines)
    else:
        network = networks[0]

    service_frame = profile.getServiceFrameShared(network, route_points, destination_displays, scheduled_stop_points, timing_points, timing_links, service_links, stop_assignments)
    service_calendar_frame = profile.getServiceCalendarFrameShared(day_types, day_type_assignments)

    publication_delivery: PublicationDelivery = profile.getShared([resource_frame], [service_frame], [service_calendar_frame])
    with open(f'netex-output-nordic/shared.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)


conversion("/tmp/optibus.xml", "")