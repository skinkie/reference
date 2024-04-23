import glob

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer, LxmlTreeSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import ServiceJourney, ServiceJourneyPattern, Codespace, Version, ServiceFrame, \
    JourneyPatternsInFrameRelStructure, AvailabilityCondition, ServiceCalendarFrame, TypeOfFrameRef, ScheduledStopPoint, \
    StopAssignmentsInFrameRelStructure, TimeDemandType, DirectionRef, Direction, MultilingualString, \
    DirectionsInFrameRelStructure, StopPlacesInFrameRelStructure
from refs import getIndex, getId, getRef
from servicecalendarepip import ServiceCalendarEPIPFrame
from siteframeepip import SiteFrameEPIP
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from xpathselection import get_stop_place_for_quayref

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

def conversion(input_filename: str, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    service_journeys = []
    service_journey_patterns = []
    availability_conditions = []
    time_demand_types = []
    directions = {}
    # scheduled_stop_points = []
    has_servicejourney_patterns = False

    epiap_tree = lxml.etree.parse("/tmp/NeTEx_DOVA_epiap_20240423013251.xml.gz")
    tree = lxml.etree.parse(input_filename)

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

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}TimeDemandType"):
        time_demand_type: TimeDemandType = parser.parse(element, TimeDemandType)
        time_demand_types.append(time_demand_type)



    codespace = Codespace(id="OPENOV", xmlns="OPENOV", xmlns_url="http://openov.nl/")
    version = Version(id="OPENOV:Version:1", version="1")

    used_direction_types = [sjp.direction_type for sjp in service_journey_patterns]
    for used_direction_type in used_direction_types:
        direction: Direction = Direction(id=getId(Direction, codespace, used_direction_type.value), version=version.version, name=MultilingualString(value=str(used_direction_type.value)), direction_type=used_direction_type)
        directions[used_direction_type] = direction

    for sjp in service_journey_patterns:
        sjp.direction_ref_or_direction_view = getRef(directions.get(sjp.direction_type, None))
        #if clean:
        sjp.direction_type = None

    if len(service_journeys) == 0:
        return

    # has_servicejourney_patterns = len(service_journey_patterns) > 0


    servicecalendarepip = ServiceCalendarEPIPFrame(codespace)
    service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    service_calendar_frame = ServiceCalendarFrame(id=getId(ServiceCalendarFrame, codespace, "ServiceCalendarFrame"), version="1",
                                                  type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"), service_calendar=service_calendar)

    timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys, service_journey_patterns, time_demand_types)
    timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

    service_frame: ServiceFrame
    service_frame = parser.parse(tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame"), ServiceFrame)
    #if not has_servicejourney_patterns:
    service_frame.journey_patterns = JourneyPatternsInFrameRelStructure(journey_pattern=service_journey_patterns)
    service_frame.directions = DirectionsInFrameRelStructure(direction=list(directions.values()))

    # for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
    #    scheduled_stop_point: ScheduledStopPoint
    #     scheduled_stop_point = parser.parse(element, ScheduledStopPoint)
    #     scheduled_stop_points.append(scheduled_stop_point)

    # service_frame.stop_assignments = StopAssignmentsInFrameRelStructure(
    #    stop_assignment=SiteFrameEPIP.getPassengerStopAssignments(service_frame.scheduled_stop_points.scheduled_stop_point))

    site_frame_epip = SiteFrameEPIP(codespace)
    site_frame = site_frame_epip.getSiteFrame(service_frame.scheduled_stop_points.scheduled_stop_point)

    stop_places = {}

    for stop_assignment in service_frame.stop_assignments.stop_assignment:
        stop_place = get_stop_place_for_quayref(epiap_tree, stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref)
        stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.version = stop_place.version
        stop_places[stop_place.id] = stop_place

    if len(stop_places.values()) > 0:
        site_frame.stop_places = StopPlacesInFrameRelStructure(stop_place=list(stop_places.values()))

    sjs = getIndex(service_journeys)
    keys = set(sjs.keys())
    # lxml_serializer = LxmlTreeSerializer()
    parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse(input_filename, parser=parser)
    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
        # TODO iets met 'modified' timestamp meenemen?
        if element.attrib['id'] in keys:
            element.getparent().replace(element, lxml.etree.fromstring(serializer.render(sjs[element.attrib['id']], ns_map).encode('utf-8'), parser))
            # element.getparent().replace(element, lxml_serializer.render(sjs[element.attrib['id']]))

    # if not has_servicejourney_patterns:
    element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
    element.getparent().replace(element, lxml.etree.fromstring(serializer.render(service_frame, ns_map).encode('utf-8'), parser))
    # element.getparent().replace(element, lxml_serializer.render(service_frame))

    element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
    # element.getparent().append(lxml_serializer.render(service_calendar_frame))
    # element.getparent().append(lxml_serializer.render(site_frame))

    element.getparent().append(lxml.etree.fromstring(serializer.render(service_calendar_frame, ns_map).encode('utf-8'), parser))
    element.getparent().append(lxml.etree.fromstring(serializer.render(site_frame, ns_map).encode('utf-8'), parser))


    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}versions"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}contentValidityConditions"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}VehicleModes"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}operationalContexts"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}PrivateCode"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}LinkSequenceProjectionRef"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}LinkSequenceProjection"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}AccessibilityAssessment"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}timeDemandTypes"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}OperationalContextRef"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//*"):
        if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
            element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}responsibilitySets"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DefaultResponsibilitySetRef"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}TypeOfServiceRef"):
        element.getparent().remove(element)

    for x in tree.iterfind(".//{http://www.netex.org.uk/netex}*"):
        x.attrib.pop("derivedFromVersionRef", None)
        x.attrib.pop("derivedFromObjectRef", None)
        x.attrib.pop("responsibilitySetRef", None)

    tree.write(output_filename, pretty_print=True, strip_text=True)

if __name__ == '__main__':
    for input_filename in glob.glob("/tmp/NeTEx_WSF_WSF_20240423_20240423.xml.gz"):
    # for input_filename in glob.glob("/tmp/NeTEx_ARR_NL_20240422_20240423_1416.xml.gz"):
        print(input_filename)
        output_filename = input_filename.replace('/tmp/', 'netex-output-epip/').replace('.xml.gz', '.xml')
        conversion(input_filename, output_filename)
