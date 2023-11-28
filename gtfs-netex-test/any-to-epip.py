import glob

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import ServiceJourney, ServiceJourneyPattern, Codespace, Version, ServiceFrame, \
    JourneyPatternsInFrameRelStructure, AvailabilityCondition, ServiceCalendarFrame, TypeOfFrameRef
from refs import getIndex, getId
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
    has_servicejourney_patterns = False

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

    has_servicejourney_patterns = len(service_journey_patterns) > 0

    codespace = Codespace(id="OPENOV", xmlns="OPENOV", xmlns_url="http://openov.nl/")
    version = Version(id="OPENOV:Version:1", version="1")

    servicecalendarepip = ServiceCalendarEPIPFrame(codespace)
    service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    service_calendar_frame = ServiceCalendarFrame(id=getId(ServiceCalendarFrame, codespace, "ServiceCalendarFrame"), version="1",
                                                  type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"), service_calendar=service_calendar)

    timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys, service_journey_patterns)
    timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

    if not has_servicejourney_patterns:
        service_frame: ServiceFrame
        service_frame = parser.parse(tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame"), ServiceFrame)
        service_frame.journey_patterns = JourneyPatternsInFrameRelStructure(choice=service_journey_patterns)


    sjs = getIndex(service_journeys)
    keys = set(sjs.keys())
    parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse("/tmp/Flix_Line_x400.xml", parser=parser)
    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
        # TODO iets met 'modified' timestamp meenemen?
        if element.attrib['id'] in keys:
            element.getparent().replace(element, lxml.etree.fromstring(serializer.render(sjs[element.attrib['id']], ns_map).encode('utf-8'), parser))

    if not has_servicejourney_patterns:
        element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
        element.getparent().replace(element, lxml.etree.fromstring(serializer.render(service_frame, ns_map).encode('utf-8'), parser))

    element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
    element.getparent().append(lxml.etree.fromstring(serializer.render(service_calendar_frame, ns_map).encode('utf-8'), parser))

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

    for element in tree.iterfind(".//*"):
        if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
            element.getparent().remove(element)

    for x in tree.iterfind(".//{http://www.netex.org.uk/netex}*"):
        x.attrib.pop("derivedFromVersionRef", None)
        x.attrib.pop("derivedFromObjectRef", None)

    tree.write(output_filename, pretty_print=True, strip_text=True)

if __name__ == '__main__':
    for input_filename in glob.glob("netex-output/*xml"):
        output_filename = input_filename.replace('netex-output/', 'netex-output-epip/')
        conversion(input_filename, output_filename)
        print(input_filename)