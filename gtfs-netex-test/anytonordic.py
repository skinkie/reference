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
    ServiceCalendarFrame, TypeOfFrameRef, Line
from nordicprofile import NordicProfile
from refs import getId
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile

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
    service_journey_patterns = []
    availability_conditions = []
    lines = []

    tree = lxml.etree.parse(input_filename)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
        line: Line = parser.parse(element, Line)
        lines.append(line)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}AvailabilityCondition"):
        availability_condition: AvailabilityCondition
        availability_condition = parser.parse(element, AvailabilityCondition)
        availability_conditions.append(availability_condition)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
        service_journey: ServiceJourney
        service_journey = parser.parse(element, ServiceJourney)
        service_journeys.append(service_journey)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourneyPattern"):
        service_journey_pattern: ServiceJourneyPattern
        service_journey_pattern = parser.parse(element, ServiceJourneyPattern)
        service_journey_patterns.append(service_journey_pattern)

    if len(service_journeys) == 0:
        return

    has_servicejourney_patterns = len(service_journey_patterns) > 0

    codespace = Codespace(id="OPENOV", xmlns="OPENOV", xmlns_url="http://openov.nl/")
    version = Version(id="OPENOV:Version:1", version="1")

    # servicecalendarepip = ServiceCalendarEPIPFrame(codespace)
    # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    # service_calendar_frame = ServiceCalendarFrame(id=getId(ServiceCalendarFrame, codespace, "ServiceCalendarFrame"), version="1",
                                                  # type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"),
    #                                              service_calendar=service_calendar)

    # timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys, service_journey_patterns)
    # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

    profile = NordicProfile(None, None, None)

    for line in lines:
        these_service_journeys = [service_journey for service_journey in service_journeys if service_journey.choice.ref == line.id]
        # timetabledpassingtimesprofile = TimetablePassingTimesProfile(self.codespace, self.version, service_journeys, service_journey_patterns)
        # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

        if len(these_service_journeys) > 0:
            # TODO: transform ServiceJourney to PassingTimes with JourneyPatternRef.
            timetable_frame = profile.getTimetableFrame(line, these_service_journeys)
            publication_delivery = profile.getLineDelivery(line, [], [], [timetable_frame])

            serializer_config = SerializerConfig(ignore_default_attributes=True)
            serializer_config.pretty_print = True
            serializer_config.ignore_default_attributes = True
            serializer = XmlSerializer(serializer_config)

            with open(f'netex-output-nordic/{line.id.replace(":", "_").replace("/", "_")}.xml', 'w') as out:
                serializer.write(out, publication_delivery, ns_map)

conversion("/tmp/optibus.xml", "")