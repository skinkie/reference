import glob
from decimal import Decimal, ROUND_HALF_UP
from typing import Set

from pyproj import Transformer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer, LxmlTreeSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import ServiceJourney, ServiceJourneyPattern, Codespace, Version, ServiceFrame, \
    JourneyPatternsInFrameRelStructure, AvailabilityCondition, ServiceCalendarFrame, TypeOfFrameRef, ScheduledStopPoint, \
    StopAssignmentsInFrameRelStructure, TimeDemandType, DirectionRef, Direction, MultilingualString, \
    DirectionsInFrameRelStructure, StopPlacesInFrameRelStructure, CodespacesRelStructure
from refs import getIndex, getId, getRef
from servicecalendarepip import ServiceCalendarEPIPFrame
from siteframeepip import SiteFrameEPIP
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from xpathselection import get_stop_place_for_quayref

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

def conversion(input_filename: str, epiap_filename: str, output_filename: str):
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
    codespaces = {}
    directions = {}
    # scheduled_stop_points = []
    has_servicejourney_patterns = False

    epiap_tree = lxml.etree.parse(epiap_filename)

    tree = lxml.etree.parse(input_filename)
    epiap_tree.find(".//{http://www.netex.org.uk/netex}DefaultLocationSystem").text


    transformers = {}
    epiap_default_locationsystem = epiap_tree.find(".//{http://www.netex.org.uk/netex}DefaultLocationSystem").text
    if epiap_default_locationsystem not in transformers:
        transformers[epiap_default_locationsystem] = Transformer.from_crs("EPSG:28992", "EPSG:4326")

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

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Codespace"):
        codespace: Codespace = parser.parse(element, Codespace)
        codespaces[codespace.id] = codespace

    codespace: Codespace
    if 'OPENOV' not in codespaces:
        codespace = Codespace(id="OPENOV", xmlns="OPENOV", xmlns_url="http://openov.nl/", description=MultilingualString(value="Values added during conversion"))
        codespaces[codespace.id] = codespace
    else:
        codespace = codespaces.get('OPENOV')

    if 'epip_metadata' not in codespaces:
        epip_metadata = Codespace(id="epip_metadata", xmlns="epip", xmlns_url="http://netex-cen.eu/epip", description=MultilingualString(value="EPIP metadata"))
        codespaces[epip_metadata.id] = epip_metadata

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

    service_calendar_tree = tree
    for element in service_calendar_tree.iterfind(".//{http://www.netex.org.uk/netex}AvailabilityCondition"):
        availability_condition: AvailabilityCondition
        availability_condition = parser.parse(element, AvailabilityCondition)
        availability_conditions.append(availability_condition)

    servicecalendarepip = ServiceCalendarEPIPFrame(codespace)
    service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    service_calendar_frame = ServiceCalendarFrame(id=getId(ServiceCalendarFrame, codespace, "ServiceCalendarFrame"), version="1",
                                                  type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_CALENDAR", version_ref="epip:1.0"), service_calendar=service_calendar)

    timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys, service_journey_patterns, time_demand_types)
    timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

    service_frame: ServiceFrame
    service_frame_xml = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
    if service_frame_xml is not None:
        service_frame = parser.parse(service_frame_xml, ServiceFrame)
    else:
        service_tree = tree
        # Implement here the filtering, so we only take the reference that are used and are relevant to EPIP

        service_frame_xml = service_tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
        if service_frame_xml is not None:
            service_frame = parser.parse(service_frame_xml, ServiceFrame)
        else:
            service_frame = ServiceFrame(id=getId(ServiceFrame, codespace, "1"), version="1")

    #if not has_servicejourney_patterns:
    service_frame.journey_patterns = JourneyPatternsInFrameRelStructure(journey_pattern=service_journey_patterns)
    service_frame.directions = DirectionsInFrameRelStructure(direction=list(directions.values()))

    for route_point in service_frame.route_points.route_point:
        latitude, longitude = transformers[epiap_default_locationsystem].transform(
            route_point.location.pos.value[0], route_point.location.pos.value[1])
        route_point.location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        route_point.location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        route_point.location.pos = None

    for ssp in service_frame.scheduled_stop_points.scheduled_stop_point:
        latitude, longitude = transformers[epiap_default_locationsystem].transform(
            ssp.location.pos.value[0], ssp.location.pos.value[1])
        ssp.location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        ssp.location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        ssp.location.pos = None


    # for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
    #    scheduled_stop_point: ScheduledStopPoint
    #     scheduled_stop_point = parser.parse(element, ScheduledStopPoint)
    #     scheduled_stop_points.append(scheduled_stop_point)

    # service_frame.stop_assignments = StopAssignmentsInFrameRelStructure(
    #    stop_assignment=SiteFrameEPIP.getPassengerStopAssignments(service_frame.scheduled_stop_points.scheduled_stop_point))

    site_frame_epip = SiteFrameEPIP(codespace)
    # TODO: don't create quays, if this is available. **1
    site_frame = site_frame_epip.getSiteFrame(service_frame.scheduled_stop_points.scheduled_stop_point)

    stop_places = {}

    epiap_tree = lxml.etree.parse(epiap_filename)


    processed_quays: Set[str] = set([])

    for stop_assignment in service_frame.stop_assignments.stop_assignment:
        if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:
            if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref in processed_quays:
                # Already processed, stop place is already stored
                continue

            stop_place = get_stop_place_for_quayref(epiap_tree, stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref)
            if stop_place is not None:

                # TODO: I want the handling of defaults differently, also take in account the local projection on this object
                if stop_place.centroid.location.longitude is None and stop_place.centroid.location.pos is not None:
                    latitude, longitude = transformers[epiap_default_locationsystem].transform(stop_place.centroid.location.pos.value[0], stop_place.centroid.location.pos.value[1])
                    stop_place.centroid.location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
                    stop_place.centroid.location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
                    stop_place.centroid.location.pos = None

                for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    if hasattr(quay, 'id'):
                        processed_quays.add(quay.id)

                    latitude, longitude = transformers[epiap_default_locationsystem].transform(quay.centroid.location.pos.value[0], quay.centroid.location.pos.value[1])
                    quay.centroid.location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
                    quay.centroid.location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
                    quay.centroid.location.pos = None

                stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.version = stop_place.version

                stop_places[stop_place.id] = stop_place


    # TODO: don't create quays, if this is available. **1
    if len(stop_places.values()) > 0:
        site_frame.stop_places = StopPlacesInFrameRelStructure(stop_place=list(stop_places.values()))

    sjs = getIndex(service_journeys)
    keys = set(sjs.keys())
    lxml_serializer = LxmlTreeSerializer()
    parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse(input_filename, parser=parser)
    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
        # TODO iets met 'modified' timestamp meenemen?
        if element.attrib['id'] in keys:
            element.getparent().replace(element, lxml.etree.fromstring(serializer.render(sjs[element.attrib['id']], ns_map).encode('utf-8'), parser))
            # element.getparent().replace(element, lxml_serializer.render(sjs[element.attrib['id']]))

    # if not has_servicejourney_patterns:
    # element_from_service = service_tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")

    element = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame")
    if element is not None:
        element.getparent().replace(element, lxml.etree.fromstring(serializer.render(service_frame, ns_map).encode('utf-8'), parser))
        # element.getparent().replace(element, lxml_serializer.render(service_frame))
    else:
        element = tree.find(".//{http://www.netex.org.uk/netex}TimetableFrame")
        element.append(lxml.etree.fromstring(serializer.render(service_frame, ns_map).encode('utf-8'), parser))

    element = tree.find(".//{http://www.netex.org.uk/netex}codespaces")
    if element is not None:
        # codespaces = CodespacesRelStructure(codespace_ref_or_codespace=list(codespaces.values()))
        element.clear()
        for codespace in codespaces.values():
            element.append(lxml.etree.fromstring(serializer.render(codespace, ns_map).encode('utf-8'), parser))

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

    # RouteLinks are not part of EPIP.
    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}OnwardRouteLinkRef"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}routeLinks"):
        element.getparent().remove(element)

    composite_frame_tof = tree.find(".//{http://www.netex.org.uk/netex}CompositeFrame/{http://www.netex.org.uk/netex}TypeOfFrameRef")
    if composite_frame_tof is not None:
        composite_frame_tof.attrib['ref'] = 'epip:EU_PI_NETWORK_OFFER'
        composite_frame_tof.attrib['versionRef'] = '1.0'
        composite_frame_tof.attrib.pop('version', None)

    site_frame_tof = tree.find(".//{http://www.netex.org.uk/netex}SiteFrame/{http://www.netex.org.uk/netex}TypeOfFrameRef")
    if site_frame_tof is not None:
        site_frame_tof.attrib['ref'] = 'epip:EU_PI_STOP'
        site_frame_tof.attrib['versionRef'] = '1.0'
        site_frame_tof.attrib.pop('version', None)

    service_frame_tof = tree.find(".//{http://www.netex.org.uk/netex}ServiceFrame/{http://www.netex.org.uk/netex}TypeOfFrameRef")
    if service_frame_tof is not None:
        service_frame_tof.attrib['ref'] = 'epip:EU_PI_NETWORK'
        service_frame_tof.attrib['versionRef'] = '1.0'
        service_frame_tof.attrib.pop('version', None)

    timetable_frame_tof = tree.find(".//{http://www.netex.org.uk/netex}TimetableFrame/{http://www.netex.org.uk/netex}TypeOfFrameRef")
    if timetable_frame_tof is not None:
        timetable_frame_tof.attrib['ref'] = 'epip:EU_PI_TIMETABLE'
        timetable_frame_tof.attrib['versionRef'] = '1.0'
        timetable_frame_tof.attrib.pop('version', None)

    resource_frame_tof = tree.find(".//{http://www.netex.org.uk/netex}ResourceFrame/{http://www.netex.org.uk/netex}TypeOfFrameRef")
    if resource_frame_tof is not None:
        resource_frame_tof.attrib['ref'] = 'epip:EU_PI_COMMON'
        resource_frame_tof.attrib['versionRef'] = '1.0'
        resource_frame_tof.attrib.pop('version', None)

    for epiap_default_locationsystem in tree.iterfind(".//{http://www.netex.org.uk/netex}DefaultLocationSystem"):
        epiap_default_locationsystem.text = 'EPSG:4326'

    tree.write(output_filename, pretty_print=True, strip_text=True)

if __name__ == '__main__':
    # for input_filename in glob.glob("/home/netex/sbb/PROD_NETEX_TT_1.10_CHE_SKI_2024_OEV-SCHWEIZ_TIMETABLE_84_270_202404140804.xml"):
    # for input_filename in glob.glob("/tmp/NeTEx_WSF_WSF_20240424_20240424.xml.gz"):
    # for input_filename in glob.glob("/tmp/NeTEx_ARR_NL_20240430_20240501_1418.xml.gz"):
    #    print(input_filename)
    #     output_filename = input_filename.replace('/home/netex/sbb/', 'netex-output-epip/').replace('.xml.gz', '.xml')
    #     conversion(input_filename, output_filename)

    for input_filename in glob.glob("/tmp/NeTEx_WSF_WSF_20240415_20240415.xml.gz"):
        print(input_filename)
        output_filename = input_filename.replace('/tmp/', 'netex-output-epip/').replace('.xml.gz', '.xml')
        conversion(input_filename, '/tmp/NeTEx_DOVA_epiap_20240423013251.xml.gz', output_filename)
