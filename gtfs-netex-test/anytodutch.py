import glob
import warnings
from typing import List, Dict

import pytz
from pyproj import Transformer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlTime

from availabilityconditionsprofile import AvailabilityConditionsProfile
from dutchprofile import DutchProfile
from netex import Codespace, DataSource, ResponsibilitySet, Version, Operator, OperationalContext, VehicleType, \
    TransportAdministrativeZone, MultilingualString, RoutePoint, RouteLink, Route, Line, DestinationDisplay, \
    ScheduledStopPoint, StopArea, PassengerStopAssignment, TimingPoint, TimingLink, ServiceJourneyPattern, \
    TimeDemandType, Notice, NoticeAssignment, AvailabilityCondition, OperatorView, Authority, ServiceJourney, \
    ServiceCalendar, PrivateCode, ServiceLink, LocationStructure2, Pos, AllVehicleModesOfTransportEnumeration, \
    LineRefStructure, DirectionType, PointsOnRouteRelStructure, StopPointInJourneyPattern, TimingPointInJourneyPattern, \
    PointProjection, PointRefStructure, PointOnRoute, RouteView, ProjectionsRelStructure, RoutePointRefStructure
from refs import getId, getRef
from timedemandtypesprofile import TimeDemandTypesProfile

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

def parseFromEtree(parser, tree, element, clazz) -> List:
    return [parser.parse(element, clazz) for element in tree.iterfind(f".//{element}")]

def convertReprojectLocation(location: LocationStructure2, transformer: Transformer):
    # TODO: implement a complete naive method, that reads the srs values, instead of hardcoding them.

    if transformer.target_crs == '4326':
        if location.latitude is not None and location.longitude is not None:
            return
        elif location.pos is not None:
            if len(location.pos.value) == 3:
                x, y, z = transformer.transform(location.pos.value[0], location.pos.value[1], location.pos.value[2])
            else:
                x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
                z = None
            location.latitude = x
            location.longitude = y
            location.altitude = z
            location.srs_name = 'EPSG:4326'

    else:
        target_srs_name = f"EPSG:{transformer.target_crs.to_epsg()}"

        if transformer.source_crs == '4326':
            if location.latitude is not None and location.longitude is not None:
                if location.altitude is not None:
                    x, y, z = transformer.transform(location.latitude, location.longitude, location.altitude)
                    location.pos = Pos(value=[x, y, z], srs_dimension=3, srs_name=target_srs_name)
                else:
                    x, y = transformer.transform(location.latitude, location.longitude)
                    location.pos = Pos(value=[x, y], srs_dimension=2, srs_name=target_srs_name)
            else:
                # TODO: here it actually becomes important to know the x, y, z order (lon, lat is expected now, not true)
                if location.pos.srs_dimension == 3:
                    x, y, z = transformer.transform(location.pos.value[0], location.pos.value[1], location.pos.value[2])
                    location.pos = Pos(value=[x, y, z], srs_dimension=3, srs_name=target_srs_name)
                else:
                    x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
                    location.pos = Pos(value=[x, y], srs_dimension=2, srs_name=target_srs_name)

            location.latitude = None
            location.longitude = None
            location.altitude = None
            location.srs_name = None

        elif location.pos is not None:
            if location.pos.srs_dimension == 3:
                x, y, z = transformer.transform(location.pos.value[0], location.pos.value[1], location.pos.value[2])
                location.srs_name = None
                location.pos = Pos(value=[x, y, z], srs_dimension=3, srs_name=target_srs_name)
            else:
                x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
                location.srs_name = None
                location.pos = Pos(value=[x, y], srs_dimension=2, srs_name=target_srs_name)


def mapPointToRoutePoint(point_ref, ssps: Dict[str, ScheduledStopPoint], tps: Dict[str, ScheduledStopPoint], rps: Dict[str, RoutePoint]):
    if point_ref in ssps:
        point = ssps[point_ref]
    else:
        point = tps[point_ref]

    rp: RoutePoint = TimeDemandTypesProfile.getObjectFromObject(point, RoutePoint,
                                                                point.id.replace(point.__class__.__name__, 'RoutePoint'))
    rps[point.id] = rp
    if point.projections is None:
        point.projections = ProjectionsRelStructure(
            projection_ref_or_projection=[PointProjection(id=point.id.replace(point.__class__.__name__, 'PointProjection'),
                                    version=point.version, project_to_point_ref=getRef(rp, PointRefStructure))])

    return rp

def mapPointInJourneyPattern(x, ssps: Dict[str, ScheduledStopPoint],
                             tps: Dict[str, TimingPoint],
                             tls: Dict[str, TimingLink],
                             sls: Dict[str, ServiceLink],
                             rps: Dict[str, RoutePoint],
                             rls: Dict[str, RouteLink]
                             ):
    por: PointOnRoute
    rl: RouteLink = None

    if isinstance(x, StopPointInJourneyPattern):
        x: StopPointInJourneyPattern = x
        ssp_ref = x.scheduled_stop_point_ref.ref
        rp = rps.get(ssp_ref, None)
        if rp is None:
            rp = mapPointToRoutePoint(ssp_ref, ssps, tls, rps)

        if x.onward_service_link_ref is not None:
            sl_ref = x.onward_service_link_ref.ref
            rl = rls.get(sl_ref, None)
            if rl is None:
                sl = sls[sl_ref]
                from_rp = rps.get(sl.from_point_ref.ref, None)
                if from_rp is None:
                    from_rp = mapPointToRoutePoint(sl.from_point_ref.ref, ssps, tps, rps)

                to_rp = rps.get(sl.to_point_ref.ref, None)
                if to_rp is None:
                    to_rp = mapPointToRoutePoint(sl.to_point_ref.ref, ssps, tps, rps)

                rl: RouteLink = TimeDemandTypesProfile.getObjectFromObject(sl, RouteLink, sl.id.replace('ServiceLink', 'RouteLink'))
                rl.from_point_ref = getRef(from_rp, RoutePointRefStructure)
                rl.to_point_ref = getRef(to_rp, RoutePointRefStructure)
                rls[sl_ref] = rl

        elif x.onward_timing_link_ref is not None:
            tl_ref = x.onward_timing_link_ref.ref
            rl = rls.get(tl_ref, None)
            if rl is None:
                tl = tls[tl_ref]
                # TODO: Do this in the academic correct way, using nameOfRefClass
                from_rp = rps.get(tl.from_point_ref.ref, None)
                if from_rp is None:
                    from_rp = mapPointToRoutePoint(tl.from_point_ref.ref, ssps, tps, rps)

                to_rp = rps.get(tl.to_point_ref.ref, None)
                if to_rp is None:
                    to_rp = mapPointToRoutePoint(tl.to_point_ref.ref, ssps, tps, rps)

                rl: RouteLink = TimeDemandTypesProfile.getObjectFromObject(tl, RouteLink, tl.id.replace('TimingLink', 'RouteLink'))
                rl.from_point_ref = getRef(from_rp, RoutePointRefStructure)
                rl.to_point_ref = getRef(to_rp, RoutePointRefStructure)
                rls[tl_ref] = rl

    elif isinstance(x, TimingPointInJourneyPattern):
        x: TimingPointInJourneyPattern = x
        tp_ref = x.timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref.ref
        rp = rps.get(tp_ref, None)
        if rp is None:
            tp = tps[tp_ref]
            rp: RoutePoint = TimeDemandTypesProfile.getObjectFromObject(tp, RoutePoint, tp.id.replace('TimingPoint', 'RoutePoint'))
            rps[tp_ref] = rp
            if tp.projections is None:
                tp.projections = ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=tp.id.replace('TimingPoint', 'PointProjection'), version=tp.version, project_to_point_ref=getRef(rp, PointRefStructure))])

        if x.onward_timing_link_ref is not None:
            tl_ref = x.onward_timing_link_ref.ref
            rl = rls.get(tl_ref, None)
            if rl is None:
                tl = tls[tl_ref]
                from_rp = rps.get(tl.from_point_ref.ref, None)
                if from_rp is None:
                    from_rp = mapPointToRoutePoint(tl.from_point_ref.ref, ssps, tps, rps)

                to_rp = rps.get(tl.to_point_ref.ref, None)
                if to_rp is None:
                    to_rp = mapPointToRoutePoint(tl.to_point_ref.ref, ssps, tps, rps)

                rl: RouteLink = TimeDemandTypesProfile.getObjectFromObject(tl, RouteLink, tl.id.replace('TimingLink', 'RouteLink'))
                rl.from_point_ref = getRef(from_rp, RoutePointRefStructure)
                rl.to_point_ref = getRef(to_rp, RoutePointRefStructure)
                rls[tl_ref] = rl

    por: PointOnRoute = TimeDemandTypesProfile.getObjectFromObject(x, PointOnRoute, x.id.replace('StopPointInJourneyPattern', 'PointOnRoute'))
    por.choice_1 = getRef(rp)
    if rl is not None:
        por.onward_route_link_ref = getRef(rl)
    return por

def routeFromServiceJourneyPattern(service_journey_pattern: ServiceJourneyPattern,
                                     ssps: Dict[str, ScheduledStopPoint],
                                     tps: Dict[str, TimingPoint],
                                     tls: Dict[str, TimingLink],
                                     sls: Dict[str, ServiceLink],
                                     rps: Dict[str, RoutePoint],
                                     rls: Dict[str, RouteLink]
                                   ) -> Route:
    # Idea: Copy over ServiceJourneyPattern
    route = TimeDemandTypesProfile.getObjectFromObject(service_journey_pattern, Route, service_journey_pattern.id.replace('ServiceJourneyPattern', 'Route'))
    if isinstance(service_journey_pattern.route_ref_or_route_view, RouteView):
        # TODO: alle attributen kopieren
        route.flexible_line_ref_or_line_ref = service_journey_pattern.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view

    route.points_in_sequence = PointsOnRouteRelStructure(point_on_route=[mapPointInJourneyPattern(x, ssps, tps, tls, sls, rps, rls)
                                                                         for x in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern])

    return route

import datetime
from pytz import timezone
def timeZoneConversion(sj: ServiceJourney, availability_conditions: Dict[str, AvailabilityCondition],  tz_in, tz_out):
    ac: AvailabilityCondition = availability_conditions[sj.validity_conditions_or_valid_between[0].choice[0].ref]

    # establish that the availability condition is not overlapping two transition times
    if hasattr(tz_in, "_utc_transition_times"):
        if len([x for x in tz_in._utc_transition_times if x > ac.from_date.to_datetime() and x < ac.to_date.to_datetime()]) > 0:
            print(f"{sj.id} with {ac.id} overlaps day light transition, journey must be duplicated!")

    if hasattr(tz_out, "_utc_transition_times"):
        if len([x for x in tz_out._utc_transition_times if
                x > ac.from_date.to_datetime() and x < ac.to_date.to_datetime()]) > 0:
            print(f"{sj.id} with {ac.id} overlaps day light transition, journey must be duplicated!")

    original_departure_time = (datetime.datetime.combine(ac.from_date.to_datetime().date(), sj.departure_time.to_time(), tzinfo=tz_in) + datetime.timedelta(days=sj.departure_day_offset or 0))
    projected_departure_time = original_departure_time.astimezone(tz_out)

    naive_offset = datetime.datetime.combine(datetime.date.min, projected_departure_time.time()) - datetime.datetime.combine(datetime.date.min, original_departure_time.time())

    sj.departure_time = XmlTime(projected_departure_time.hour, projected_departure_time.minute, projected_departure_time.second)
    if naive_offset.days != 0:
        sj.departure_day_offset = naive_offset.days * -1
    else:
        sj.departure_day_offset = None

def conversion(input_filename: str, output_filename: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    tree = lxml.etree.parse(input_filename)

    codespaces: List[Codespace] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Codespace", Codespace)

    versions: List[Version] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Version", Version)
    if len(versions) == 0:
        versions.append(Version(id=getId(Version, codespaces[0], "1"), version="1"))

    data_sources: List[DataSource] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Datasource", DataSource)
    if len(data_sources) == 0:
        data_sources.append(DataSource(id=getId(DataSource, codespaces[0], "OPENOV"), version=versions[0].version, name=MultilingualString(value="openOV"), short_name=MultilingualString(value="OPENOV")))

    responsibility_sets: List[ResponsibilitySet] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ResponsibilitySet", ResponsibilitySet)

    operators: List[Operator] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Operator", Operator)

    authorities: List[Authority] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Authority", Authority)

    operational_contexts: List[OperationalContext] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}OperatinalContext", OperationalContext)


    vehicle_types: List[VehicleType] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}VehicleType", VehicleType)

    transport_administrative_zones: List[TransportAdministrativeZone] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}TransportAdministrativeZone", TransportAdministrativeZone)

    route_points: List[RoutePoint] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}RoutePoint", RoutePoint)

    # TODO: 4326 is a guess here too, might need to be based on FrameDefaults
    transformer = Transformer.from_crs(4326, 28992)
    [convertReprojectLocation(x.location, transformer) for x in route_points if x.location is not None]

    route_links: List[RouteLink] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}RouteLink", RouteLink)
    # TODO: route link may have shape

    routes: List[Route] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Route", Route)

    lines: List[Line] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Line", Line)
    if len(lines):
        # TODO: Introduce a single operator line?
        pass

    if len(operational_contexts) == 0:
        operational_contexts += [OperationalContext(id=getId(OperationalContext, codespaces[0], str(tm)), version=versions[0].version, vehicle_mode=AllVehicleModesOfTransportEnumeration(tm)) for tm in set([line.transport_mode for line in lines])]

    destination_displays: List[DestinationDisplay] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}DestinationDisplay", DestinationDisplay)

    scheduled_stop_points: List[ScheduledStopPoint] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ScheduledStopPoint", ScheduledStopPoint)
    [convertReprojectLocation(x.location, transformer) for x in scheduled_stop_points if x.location is not None]

    stop_areas: List[StopArea] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}StopArea", StopArea)

    stop_assignments: List[PassengerStopAssignment] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}PassengerStopAssignment", PassengerStopAssignment)

    timing_points: List[TimingPoint] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}TimingPoint", TimingPoint)
    [convertReprojectLocation(x.location, transformer) for x in timing_points if x.location is not None]

    timing_links: List[TimingLink] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}TimingLink", TimingLink)
    # TODO: timing link may have shape

    service_links: List[ServiceLink] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ServiceLink", ServiceLink)
    # TODO: service link may have shape

    service_journeys: List[ServiceJourney] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ServiceJourney", ServiceJourney)

    service_journey_patterns: List[ServiceJourneyPattern] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ServiceJourneyPattern", ServiceJourneyPattern)

    time_demand_types: List[TimeDemandType] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}TimeDemandType", TimeDemandType)

    tdtp = TimeDemandTypesProfile(codespace=codespaces[0], version=versions[0])

    if len(service_journey_patterns) == 0 or len(time_demand_types) == 0:
        ssps = {x.id: x for x in scheduled_stop_points}
        tls = {x.id: x for x in timing_links}
        sls = {x.id: x for x in service_links}
        sjps = {x.id: x for x in service_journey_patterns}
        sjps_hash = {TimeDemandTypesProfile.getServiceJourneyPatternHash(x): x.id for x in service_journey_patterns}
        tdts = {x.id: x for x in time_demand_types}
        tdts_hash = {TimeDemandTypesProfile.getTimeDemandTypeHash(x): x.id for x in time_demand_types}

        for sj in service_journeys:
            tdtp.getServiceJourneyPattern(sj, sjps, sjps_hash, ssps, tls)
            tdtp.getTimeDemandType(sj, sjps, tdts, tdts_hash, ssps, tls, sls)

        service_journey_patterns = list(sjps.values())
        time_demand_types = list(tdts.values())
        timing_links = list(tls.values())

    if len(routes) == 0:
        ssps = {x.id: x for x in scheduled_stop_points}
        tps = {x.id: x for x in timing_points}
        tls = {x.id: x for x in timing_links}
        sls = {x.id: x for x in service_links}
        rps = {x.id: x for x in route_points} # TODO: dit werkt niet, want we gebruiken in
        rls = {x.id: x for x in route_links}  # TODO: de functie niet het id als key

        for sjp in service_journey_patterns:
            route = routeFromServiceJourneyPattern(sjp, ssps, tps, tls, sls, rps, rls)
            sjp.route_ref_or_route_view = getRef(route)
            routes.append(route)

        route_points = list(rps.values())
        route_links = list(rls.values())

    if len(vehicle_types) == 0:
        vt = VehicleType(id=getId(VehicleType, codespaces[0], "UNKNOWN"), version=versions[0].version, name=MultilingualString(value="Onbekend"))
        vehicle_types.append(vt)
        vt_ref = getRef(vt)
        for sj in service_journeys:
            sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = vt_ref

    for sj in service_journeys:
        sj.private_code = PrivateCode(type_value="JourneyNumber",
                                      value=str(int(str(sj.departure_time).replace(':', ''))))

    notices: List[Notice] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}Notice", Notice)

    notice_assignments: List[NoticeAssignment] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}NoticeAssignment", NoticeAssignment)


    availability_conditions: List[AvailabilityCondition] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}AvailabilityCondition", AvailabilityCondition)
    if len(availability_conditions) == 0:
        acp  = AvailabilityConditionsProfile(codespaces[0], versions[0])

        # TODO: add a profile guesser
        service_calendars: List[ServiceCalendar] = parseFromEtree(parser, tree, "{http://www.netex.org.uk/netex}ServiceCalendar", ServiceCalendar)
        availability_conditions, service_journeys = acp.fromEPIPServiceCalendar(service_calendars, service_journeys)


    # TODO: snif from FrameDefaults
    tz_in = pytz.timezone("UTC")
    tz_out = pytz.timezone("Europe/Amsterdam")
    acs = {x.id: x for x in availability_conditions}
    for sj in service_journeys:
        timeZoneConversion(sj, acs, tz_in,tz_out)
    for operator in operators:
        operator.locale.time_zone = None
        operator.locale.summer_time_zone = None
        operator.locale.time_zone_offset = None

    dutchprofile = DutchProfile(codespaces[0], data_sources[0], versions[0])
    resource_frames = dutchprofile.getResourceFrames(data_sources=data_sources, responsibility_sets=responsibility_sets,
                                                     organisations=operators + authorities, operational_contexts=operational_contexts,
                                                     vehicle_types=vehicle_types, zones=transport_administrative_zones)


    service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                                   destination_displays=destination_displays,
                                                   scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                                  stop_assignments=stop_assignments, timing_points=timing_points, timing_links=timing_links,
                                                   service_journey_patterns=service_journey_patterns, time_demand_types=time_demand_types,
                                                  notices=notices, notice_assignments=notice_assignments)

    timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions,
                                                      operator_view=OperatorView(operator_ref=getRef(operators[0])),
                                                      vehicle_journeys=service_journeys)

    composite_frame = dutchprofile.getCompositeFrame(codespaces=codespaces, versions=versions,
                                                     resource_frames=resource_frames, service_frames=service_frames,
                                                     timetable_frames=timetable_frames)

    publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste universele export")

    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    with open('netex-output/dutch.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)

    parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse("netex-output/dutch.xml", parser=parser)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}passingTimes"):
        element.getparent().remove(element)

    for element in tree.iterfind(".//*"):
        if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
            element.getparent().remove(element)

    for x in tree.iterfind(".//{http://www.netex.org.uk/netex}*"):
        x.attrib.pop("derivedFromVersionRef", None)
        x.attrib.pop("derivedFromObjectRef", None)


    for element in tree.iterfind(".//*"):
        if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
            element.getparent().remove(element)
    tree.write("netex-output/dutch-filter.xml", pretty_print=True, strip_text=True)

if __name__ == '__main__':
    for input_filename in glob.glob("netex-output-epip/Flix_Line_025.xml"):
        print(input_filename)
        output_filename = input_filename.replace('netex-output/', 'netex-output-epip/')
        conversion(input_filename, output_filename)
