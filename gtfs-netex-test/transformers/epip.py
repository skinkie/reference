import sys
import warnings
from datetime import datetime, date
from decimal import Decimal, ROUND_HALF_UP
from functools import partial
from itertools import chain
from multiprocessing import Pool
from typing import Generator, List, Dict

import netex_monkeypatching

from aux_logging import log_print
from utils import project, chain, GeneratorTester

from xsdata.models.datatype import XmlDateTime, XmlDate

from callsprofile import CallsProfile

from configuration import defaults

from netex import PublicationDelivery, ParticipantRef, MultilingualString, DataObjectsRelStructure, GeneralFrame, \
    GeneralFrameMembersRelStructure, ServiceJourney, StopPlace, CompositeFrame, FramesRelStructure, TimetableFrame, \
    JourneysInFrameRelStructure, TypeOfFrame, TypeOfFrameRef, ServiceFrame, JourneyPatternsInFrameRelStructure, \
    DirectionsInFrameRelStructure, ServiceJourneyPattern, Direction, RoutePointsInFrameRelStructure, RoutePoint, \
    ScheduledStopPointsInFrameRelStructure, ScheduledStopPoint, RoutesInFrameRelStructure, Route, \
    LinesInFrameRelStructure, Line, SiteFrame, ResourceFrame, CodespacesRelStructure, Codespace, \
    StopPlacesInFrameRelStructure, ServiceFacilitySet, DataSourcesInFrameRelStructure, OrganisationsInFrameRelStructure, \
    VehicleTypesInFrameRelStructure, ResponsibilitySetsInFrameRelStructure, DataSource, Authority, Operator, \
    VehicleType, ResponsibilitySet, Branding, RouteLinksInFrameRelStructure, RouteLink, Network, \
    NetworksInFrameRelStructure, DestinationDisplaysInFrameRelStructure, DestinationDisplay, \
    ServiceLinksInFrameRelStructure, ServiceLink, TransfersInFrameRelStructure, StopAssignmentsInFrameRelStructure, \
    PassengerStopAssignment, Connection, SiteConnection, DefaultConnection, ServiceCalendarFrame, \
    DayTypesInFrameRelStructure, ServiceCalendar, DayType, FlexibleLine, VersionFrameDefaultsStructure, SystemOfUnits, \
    LocaleStructure, Notice, NoticeAssignment, NoticesInFrameRelStructure, NoticeAssignmentsInFrameRelStructure, \
    TopographicPlacesInFrameRelStructure, TopographicPlace, TransportOrganisationVersionStructure, Locale, \
    TypesOfValueInFrameRelStructure, ValueSet, ValidityConditionsRelStructure, AvailabilityCondition, JourneyMeeting, \
    InterchangeRule, JourneyMeetingsInFrameRelStructure, InterchangeRulesInFrameRelStructure, TariffZone, \
    TariffZonesInFrameRelStructure, ZonesInFrameRelStructure, TransportAdministrativeZone, ServiceJourneyInterchange, \
    JourneyInterchangesInFrameRelStructure, UicOperatingPeriod, DayTypeAssignment, AvailabilityConditionRef, \
    OperatingPeriodRef, DayTypeRefsRelStructure, DayTypesRelStructure, OperatingPeriodsRelStructure, \
    DayTypeAssignmentsRelStructure, RouteView, LineRef, FlexibleLineRef, RouteRef, TimetabledPassingTimesRelStructure, \
    TimeDemandType, Quay, StopPointInJourneyPattern, PointsInJourneyPatternRelStructure, \
    TransportOrganisationRefsRelStructure

from netexio.database import Database

from netexio.dbaccess import load_generator, load_local, write_generator, write_objects, get_single, \
    recursive_attributes, fetch_references_classes_generator
from refs import getIndex, getRef, getId
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from transformers.projection import project_location_4326, project_polygon
from transformers.timetabled_passing_time import infer_id_and_order_and_apply
from utils import project

EPIP_CLASSES = [ "Codespace", "StopPlace", "RoutePoint", "RouteLink", "Routes", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "ServiceJourneyPattern", "PassengerStopAssignment", "Notice", "NoticeAssignment", "AvailabilityCondition" ]

def epip_line_generator(db_read: Database, db_write: Database, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(line: Line):
        line.branding_ref = None
        line.type_of_service_ref = None
        line.type_of_product_category_ref = None
        if line.operator_ref and line.authority_ref:
            if defaults['authority_reference']:
                if line.additional_operators and line.additional_operators.transport_organisation_ref:
                    line.additional_operators.transport_organisation_ref.append(line.operator_ref)
                else:
                    line.additional_operators = TransportOrganisationRefsRelStructure(transport_organisation_ref=[line.operator_ref])
                line.operator_ref = None
            else:
                if line.additional_operators and line.additional_operators.transport_organisation_ref:
                    line.additional_operators.transport_organisation_ref.append(line.authority_ref)
                else:
                    line.additional_operators = TransportOrganisationRefsRelStructure(transport_organisation_ref=[line.authority_ref])
                line.authority_ref = None

        return line

    def query(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, Line)
        for line in pool.imap_unordered(process, _load_generator, chunksize=100):
            yield line

    write_generator(db_write, Line, query(db_read), True)

def epip_line_memory(db_read: Database, db_write: Database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    lines: List[Line] = load_local(db_read, Line)
    for line in lines:
        line: Line
        line.branding_ref = None
        line.type_of_service_ref = None
        line.type_of_product_category_ref = None
        if line.operator_ref and line.authority_ref:
            if defaults['authority_reference']:
                if line.additional_operators and line.additional_operators.transport_organisation_ref:
                    line.additional_operators.transport_organisation_ref.append(line.operator_ref)
                else:
                    line.additional_operators = TransportOrganisationRefsRelStructure(transport_organisation_ref=[line.operator_ref])
                line.operator_ref = None
            else:
                if line.additional_operators and line.additional_operators.transport_organisation_ref:
                    line.additional_operators.transport_organisation_ref.append(line.authority_ref)
                else:
                    line.additional_operators = TransportOrganisationRefsRelStructure(transport_organisation_ref=[line.authority_ref])
                line.authority_ref = None

    write_objects(db_write, lines, True, True)

def epip_scheduled_stop_point_generator(db_read: Database, db_write: Database, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        ssp.stop_areas = None
        ssp.key_list = None
        ssp.extensions = None
        project_location_4326(ssp.location)
        return ssp

    def query(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ScheduledStopPoint)
        for ssp in pool.imap_unordered(partial(process, generator_defaults=generator_defaults), _load_generator, chunksize=100):
            yield ssp

    write_generator(db_write, ScheduledStopPoint, query(db_read), True)

def epip_scheduled_stop_point_memory(db_read: Database, db_write: Database, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)

    scheduled_stop_points = load_local(db_read, ScheduledStopPoint)
    for ssp in scheduled_stop_points:
        ssp: ScheduledStopPoint
        ssp.stop_areas = None
        if ssp.location is not None:
            project_location_4326(ssp.location)
        else:
            print(f"ScheduledStopPoint {ssp.id} does not have a location.")

    write_objects(db_write, scheduled_stop_points, True, True)

def epip_site_frame_memory(db_read: Database, db_write: Database, generator_defaults):
    print(sys._getframe().f_code.co_name)

    stop_places: dict[str, StopPlace] = getIndex(load_local(db_read, StopPlace))

    # Resolving a quay is very expensive. Either in the database it should be stored independently, or an index should be made available.
    quays: dict[str, Quay] = getIndex([quay for quay in chain(*[stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay for stop_place in stop_places.values() if stop_place.quays is not None]) if isinstance(quay, Quay)])

    refs = set([])

    stop_assignments: List[PassengerStopAssignment] = load_local(db_read, PassengerStopAssignment)
    retain_stop_assignments = []
    for stop_assignment in stop_assignments:
        if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:  # and 'NL:Q:' in stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref:
            # TODO: Shouldn't be done here
            stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref.replace('NL:Q:', 'NL:CHB:Quay:')
            quay: Quay = quays.get(stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref)
            if quay is not None:
                stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.version = quay.version
                refs.add(quay.id)
            else:
                stop_assignment.taxi_stand_ref_or_quay_ref_or_quay = None

        if stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:  # and 'NL:S:' in stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref:
            # TODO: Shouldn't be done here
            stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref.replace('NL:S:', 'NL:CHB:StopPlace:')
            stop_place: StopPlace = stop_places.get(stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref)
            if stop_place is not None:
                stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.version = stop_place.version
                refs.add(stop_place.id)
            else:
                stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place = None

        if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None or stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:
            retain_stop_assignments.append(stop_assignment)

    if len(retain_stop_assignments) > 0:
        write_objects(db_write, retain_stop_assignments, True, True)

    stop_places: List[StopPlace] = load_local(db_read, StopPlace)
    retained_stop_places: List[StopPlace] = []
    for stop_place in stop_places:
        keep = False
        if stop_place.id in refs:
            keep = True
        else:
            if stop_place.quays:
                for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    if quay.id in refs:
                        keep = True
                        break

        if not keep:
            continue

        stop_place.extensions = None
        stop_place.key_list = None

        """
        stop_place.equipment_places = None
        if stop_place.access_spaces is not None:
            for access_space in stop_place.access_spaces.access_space_ref_or_access_space:
                if isinstance(access_space, AccessSpace):
                    access_space: AccessSpace
                    if access_space.polygon_or_multi_surface:
                        # TODO: Shouldn't be done here
                        access_space.polygon_or_multi_surface.srsName = "urn:ogc:def:crs:EPSG::4326"
                        access_space.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                            0].value = [
                            Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in
                            access_space.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                0].value]
        
        if stop_place.quays:
            for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                if isinstance(quay, Quay):
                    quay: Quay
                    if quay.polygon_or_multi_surface:
                        # Reverse order of elements
                        yy = quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                 0].value[0::2]
                        xx = quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                 0].value[1::2]
                        quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list = [
                            PosList(value=list(chain(*zip(xx, yy))))]

                        project_polygon(quay.polygon_or_multi_surface, 'urn:ogc:def:crs:EPSG::4326')

                    if quay.centroid:
                        project_location_4326(quay.centroid.location)

        if stop_place.centroid:
            project_location_4326(stop_place.centroid.location)
        """
        retained_stop_places.append(stop_place)

    write_objects(db_write, retained_stop_places, True, True)

def epip_timetabled_passing_times_memory(db_read: Database, db_write: Database, generator_defaults, dynamics=[]):
    print(sys._getframe().f_code.co_name)

    # TODO: Maybe do this on the fly, per servicejourney?
    service_journey_patterns: List[ServiceJourneyPattern] = load_local(db_read, ServiceJourneyPattern)
    time_demand_types = load_local(db_read, TimeDemandType)
    service_journeys = load_local(db_read, ServiceJourney)

    timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

    # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
    timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)
    time_demand_types = None

    availability_conditions = load_local(db_read, AvailabilityCondition)
    servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
    service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
    write_objects(db_write, [service_calendar], True, False)

    for sj in service_journeys:
        sj: ServiceJourney
        sj.validity_conditions_or_valid_between = None
        sj.key_list = None
        sj.private_code = None

        # TODO: Benchmark
        any(map(lambda x: x(sj), dynamics))
        # for dynamic in dynamics:
        #     dynamic(sj)

    write_objects(db_write, service_journeys, True, False)

import hashlib

# TODO: Potentially refactor this
def service_journey_pattern_from_calls(sj: ServiceJourney, generator_defaults: dict):
    piss: List[StopPointInJourneyPattern] = []

    # Because NeTEx only support LineRef from a Route, and a ServiceJourneyPattern can refer to a single Route
    # we must make our new ServiceJourneyPattern unique by Line.
    l_ssp = [sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view.ref]

    for call in sj.calls.call:
        call.extensions = None
        pis: StopPointInJourneyPattern = project(call, StopPointInJourneyPattern)
        pis.scheduled_stop_point_ref = call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view
        piss.append(pis)
        l_ssp.append(pis.scheduled_stop_point_ref.ref)

    id = hashlib.md5(';'.join(l_ssp).encode()).hexdigest()[0:8]

    for pis in piss:
        pis.id = getId(StopPointInJourneyPattern, generator_defaults['codespace'], f"{id}-{pis.order}")

    return ServiceJourneyPattern(id=getId(ServiceJourneyPattern, generator_defaults['codespace'], id), version=sj.version,
                                 route_ref_or_route_view=RouteView(flexible_line_ref_or_line_ref_or_line_view=sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view),
                                 direction_type=sj.direction_type,
                                 points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=piss))


def service_journey_ac_to_day_type(service_journey: ServiceJourney,
                                   availability_conditions: Dict[str, AvailabilityCondition],
                                   day_types: Dict[str, DayType],
                                   uic_operating_periods: List[UicOperatingPeriod],
                                   day_type_assignments: List[DayTypeAssignment]):
    acs = []

    for ac in service_journey.validity_conditions_or_valid_between:
        if isinstance(ac, ValidityConditionsRelStructure):
            ac: ValidityConditionsRelStructure
            for a in ac.choice:
                if isinstance(a, AvailabilityConditionRef):
                    acs.append(availability_conditions[a.ref])
                elif isinstance(a, AvailabilityCondition):
                    acs.append(a)
                else:
                    warnings.warn(f"Unhandled ValidityCondition in {service_journey.id}")

    if service_journey.day_types is not None:
        if len(acs) == 0:
            # There are no AvailabilityConditions, TODO: there may be ValidBetweens, trust the DayType
            return
        else:
            # Both exist, maybe trigger a warning?
            pass    


    # TODO: this will fail in extreme cases
    if len(acs) > 0:
        day_type_id = acs[0].id.replace('AvailabilityCondition', 'DayType')
    else:
        warnings.warn(f'Check {service_journey.id}')
        return

    if day_type_id not in day_types:
        valid_days, days_of_week = ServiceCalendarEPIPFrame.positiveAvailabilityCondition(acs)

        if len(valid_days) == 0:
            warnings.warn(f"{day_type_id} does not have any valid days")
            uic_operating_period = UicOperatingPeriod(id=acs[0].id.replace('AvailabilityCondition', 'UicOperatingPeriod'),
                                                      version=acs[0].version,
                                                      derived_from_object_ref=acs[0].id,
                                                      derived_from_version_ref_attribute=acs[0].version,
                                                      from_operating_day_ref_or_from_date=acs[0].from_date,
                                                      to_operating_day_ref_or_to_date=acs[0].from_date, # Since the entire string is empty anyway?
                                                      valid_day_bits="0",
                                                      days_of_week=days_of_week)
            uic_operating_periods.append(uic_operating_period)

        else:
            uic_operating_period = UicOperatingPeriod(id=acs[0].id.replace('AvailabilityCondition', 'UicOperatingPeriod'),
                                                      version=acs[0].version,
                                                      derived_from_object_ref=acs[0].id,
                                                      derived_from_version_ref_attribute=acs[0].version,
                                                      from_operating_day_ref_or_from_date=XmlDateTime.from_datetime(
                                                          valid_days[0]),
                                                      to_operating_day_ref_or_to_date=XmlDateTime.from_datetime(
                                                          valid_days[-1]),
                                                      valid_day_bits=ServiceCalendarEPIPFrame.valid_days_to_bits(
                                                          valid_days),
                                                      days_of_week=days_of_week)
            uic_operating_periods.append(uic_operating_period)

        day_type = DayType(id=day_type_id, version=service_journey.version,
                           derived_from_object_ref=service_journey.id,
                           derived_from_version_ref_attribute=service_journey.version)
        day_types[day_type_id] = day_type

        day_type_assignment = DayTypeAssignment(id=acs[0].id.replace('AvailabilityCondition', 'DayTypeAssignment'),
                                                version=acs[0].version,
                                                order=1,
                                                derived_from_object_ref=acs[0].id,
                                                derived_from_version_ref_attribute=acs[0].version,
                                                uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date=getRef(
                                                    uic_operating_period, OperatingPeriodRef),
                                                day_type_ref=getRef(day_type)
                                                )
        day_type_assignments.append(day_type_assignment)

    day_type = day_types[day_type_id]
    service_journey.day_types = DayTypeRefsRelStructure(day_type_ref=[getRef(day_type)])

def get_service_calendar(day_types: Dict[str, DayType],
                     uic_operating_periods: List[UicOperatingPeriod],
                     day_type_assignments: List[DayTypeAssignment],
                     generator_defaults: dict):
    from_date: datetime
    to_date: datetime

    if len(uic_operating_periods) == 0:
        warnings.warn("No uic_operating_periods available, submit this example to github")

    from_date = min([uic.from_operating_day_ref_or_from_date.to_datetime() for uic in uic_operating_periods])
    to_date = max([uic.to_operating_day_ref_or_to_date.to_datetime() for uic in uic_operating_periods])

    return ServiceCalendar(id=getId(ServiceCalendar, generator_defaults['codespace'], "ServiceCalendar"),
                           version=generator_defaults['version'],
                           from_date=XmlDate.from_date(from_date.date()), to_date=XmlDate.from_date(to_date.date()),
                           day_types=DayTypesRelStructure(day_type_ref_or_day_type=list(day_types.values())),
                           operating_periods=OperatingPeriodsRelStructure(uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period=uic_operating_periods),
                           day_type_assignments=DayTypeAssignmentsRelStructure(day_type_assignment=day_type_assignments))

def epip_service_journey_generator(db_read: Database, db_write: Database, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)
    sjps: Dict[str, ServiceJourneyPattern] = {}
    availability_conditions: Dict[str, AvailabilityCondition] = {}
    day_types: Dict[str, DayType] = {}
    uic_operating_periods: List[UicOperatingPeriod] = []
    day_type_assignments: List[DayTypeAssignment] = []

    def recover_line_ref(service_journey: ServiceJourney, service_journey_pattern: ServiceJourneyPattern, db_read):
        sj_line_ref = None
        if service_journey.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view is not None and (isinstance(service_journey.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view, FlexibleLineRef) or isinstance(service_journey.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view, LineRef)):
            sj_line_ref = service_journey.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view

        if service_journey_pattern.route_ref_or_route_view is not None:
            if isinstance(service_journey_pattern.route_ref_or_route_view, RouteView):
                if isinstance(
                        service_journey_pattern.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view,
                        LineRef) or isinstance(
                        service_journey_pattern.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view,
                        FlexibleLineRef):
                    # There is already an existing LineRef, overwriting is not smart.
                    pass
                else:
                    if sj_line_ref is not None:
                        service_journey_pattern.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view = sj_line_ref
                        sjps[service_journey_pattern.id] = service_journey_pattern
                    else:
                        print("RouteView: Other options to recover line not available")

            elif isinstance(service_journey_pattern.route_ref_or_route_view, RouteRef):
                route: Route = get_single(db_read, Route, service_journey_pattern.route_ref_or_route_view.ref,
                                          service_journey_pattern.route_ref_or_route_view.version)
                service_journey_pattern.route_ref_or_route_view = RouteView(
                    flexible_line_ref_or_line_ref_or_line_view=route.line_ref)
                sjps[service_journey_pattern.id] = service_journey_pattern

                if service_journey_pattern.direction_type is None:
                    service_journey_pattern.direction_type = route.direction_type.value

                if service_journey_pattern.direction_ref_or_direction_view is None:
                    service_journey_pattern.direction_ref_or_direction_view = route.direction_ref

                if service_journey_pattern.distance is None:
                    route.distance = service_journey_pattern.distance

        else:
            service_journey_pattern.route_ref_or_route_view = RouteView(flexible_line_ref_or_line_ref_or_line_view=sj_line_ref)
            sjps[service_journey_pattern.id] = service_journey_pattern

    def process(sj: ServiceJourney, db_read: Database, db_write: Database, generator_defaults: dict):
        sj: ServiceJourney

        # Prototype, just: TimeDemandType -> PassingTimes
        service_journey_pattern: ServiceJourneyPattern = None

        if sj.passing_times:
            service_journey_pattern: ServiceJourneyPattern = get_single(db_read, ServiceJourneyPattern,
                                                                        sj.journey_pattern_ref.ref,
                                                                        sj.journey_pattern_ref.version)

            # Since we don't do it ourselves, we might want to check the poor input offered.
            infer_id_and_order_and_apply(sj)

        elif sj.calls:
            if sj.journey_pattern_ref:
                service_journey_pattern: ServiceJourneyPattern = get_single(db_read, ServiceJourneyPattern,
                                                                            sj.journey_pattern_ref.ref,
                                                                            sj.journey_pattern_ref.version)
            else:
                service_journey_pattern = service_journey_pattern_from_calls(sj, generator_defaults)
                sj.journey_pattern_ref = getRef(service_journey_pattern)
                sjps[service_journey_pattern.id] = service_journey_pattern

            sj.passing_times = TimetabledPassingTimesRelStructure(timetabled_passing_time=TimetablePassingTimesProfile.getTimetabledPassingtimesFromCalls(sj, service_journey_pattern))

        elif sj.time_demand_type_ref:
            service_journey_pattern: ServiceJourneyPattern = get_single(db_read, ServiceJourneyPattern,
                                                                        sj.journey_pattern_ref.ref,
                                                                        sj.journey_pattern_ref.version)
            time_demand_type: TimeDemandType = get_single(db_read, TimeDemandType, sj.time_demand_type_ref.ref,
                                                          sj.time_demand_type_ref.version)
            CallsProfile.getPassingTimesFromTimeDemandType(sj, service_journey_pattern, time_demand_type)

        recover_line_ref(sj, service_journey_pattern, db_read)

        service_journey_ac_to_day_type(sj, availability_conditions, day_types, uic_operating_periods, day_type_assignments)

        # TODO: AvailabilityCondition -> Uic

        sj.validity_conditions_or_valid_between = None
        sj.time_demand_type_ref = None
        sj.key_list = None
        sj.private_code = None
        sj.train_numbers = None
        sj.extensions = None
        sj.notice_assignments = None
        sj.calls = None
        return sj

    def query(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ServiceJourney)
        for sj in _load_generator:
            yield process(sj, db_read, db_write, generator_defaults)
        # for sj in pool.imap_unordered(partial(process, read_database=read_database, write_database=write_database, generator_defaults=generator_defaults), _load_generator, chunksize=100):
        #     yield sj

    availability_conditions = getIndex(load_local(db_read, AvailabilityCondition))

    write_generator(db_write, ServiceJourney, query(db_read), True)

    # This check is a bit naive, if mixed files would exists, still not all ServiceJourneyPatterns would be available.
    # If we would instead 'mix' the Original + the generated one, that would also be an issue for anything that would have updated the object.
    if len(sjps.values()) > 0:
        write_objects(db_write, list(sjps.values()), True, True)

    # Until we can persistently attach database this doesnot make sense
    # else:
    #    attach_objects(db_write, read_database, ServiceJourneyPattern)

    if len(uic_operating_periods) == 0:
        service_calendars: List[ServiceCalendar] = load_local(db_read, ServiceCalendar)
        # TODO: WORKAROUND
        write_objects(db_write, service_calendars, True, True)

        # TODO
        # day_types = getIndex(list(chain.from_iterable([service_calendar.day_types.day_type_ref_or_day_type for service_calendar in service_calendars if service_calendar.day_types])) + load_local(db_read, DayType))
        # uic_operating_periods = list(chain.from_iterable([service_calendar.operating_periods.uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period for service_calendar in service_calendars if service_calendar.operating_periods] + load_local(db_read, UicOperatingPeriod)))
        # day_type_assignments = list(chain.from_iterable([service_calendar.day_type_assignments.day_type_assignment for service_calendar in service_calendars if service_calendar.day_type_assignments]))

    else:
        # TODO: Quick "fix" this should be done differently, because we cannot assure that the ServiceCalendar stored, is actually following EPIP.
        service_calendar = get_service_calendar(day_types, uic_operating_periods, day_type_assignments, generator_defaults)
        write_objects(db_write, [service_calendar], True, True)

    # availability_conditions = load_local(db_read, AvailabilityCondition)
    # servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
    # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys,
    #                                                                                availability_conditions)
    # write_objects(write_con, [service_calendar], True, False)

    # timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

        # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
        # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

        # availability_conditions = load_local(db_read, AvailabilityCondition)
        # servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
        # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
        # write_objects(write_con, [service_calendar], True, False)

def epip_remove_keylist_extensions(db_read: Database, db_write: Database, generator_defaults: dict):
    def process(deserialised, keys: List):
        for obj, path in recursive_attributes(deserialised, []):
            for key in keys:
                if hasattr(obj, key):
                    obj.key = None

        return deserialised

    def query1(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, StopPlace)
        for obj in _load_generator:
            yield process(obj, ['key_list', 'extensions'])

    def query2(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ScheduledStopPoint)
        for obj in _load_generator:
            yield process(obj, ['key_list', 'extensions'])

    def query3(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ServiceJourneyPattern)
        for obj in _load_generator:
            yield process(obj, ['key_list', 'extensions'])

    def query4(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ServiceJourney)
        for obj in _load_generator:
            yield process(obj, ['key_list', 'extensions'])

    write_generator(db_write, StopPlace, query1(db_read))
    write_generator(db_write, ScheduledStopPoint, query2(db_read))
    write_generator(db_write, ServiceJourneyPattern, query3(db_read))
    write_generator(db_write, ServiceJourney, query4(db_read))


def export_epip_network_offer(db_orig: Database, db_target: Database) -> PublicationDelivery:
    # The way how con_orig, and con_target have been modelled, is too hardcoded.
    # An alternative would be to put all the contents in the con_target.
    # TODO: Refactor to a single db_target

    codespace_ref_or_codespace = GeneratorTester(load_generator(db_orig, Codespace))
    data_source = GeneratorTester(load_generator(db_orig, DataSource))
    organisation_or_transport_organisation = load_local(db_orig, Authority) + load_local(db_orig, Operator)
    value_set = GeneratorTester(load_generator(db_orig, ValueSet))
    transport_administrative_zone = GeneratorTester(load_generator(db_orig, TransportAdministrativeZone))

    all_locales = {org.locale for org in organisation_or_transport_organisation if org.locale is not None}
    if len(all_locales) > 1:
        log_print("TODO: Test case for multiple TimetableFrames!")

    transport_type_dummy_type_or_train_type = GeneratorTester(load_generator(db_orig, VehicleType))
    responsibility_set = GeneratorTester(load_generator(db_target, ResponsibilitySet))

    stop_place = GeneratorTester(load_generator(db_target, StopPlace))
    topographic_place = GeneratorTester(load_generator(db_orig, TopographicPlace))

    direction = GeneratorTester(load_generator(db_target, Direction))
    line = GeneratorTester(chain(load_generator(db_target, Line), load_generator(db_orig, FlexibleLine)))
    network = GeneratorTester(load_generator(db_orig, Network, 0))
    # network = GeneratorTester(load_generator(db_orig, Network, 1))
    destination_display = GeneratorTester(load_generator(db_orig, DestinationDisplay))
    scheduled_stop_point = GeneratorTester(load_generator(db_target, ScheduledStopPoint))
    tariff_zone = GeneratorTester(load_generator(db_target, TariffZone))
    service_link = GeneratorTester(load_generator(db_target, ServiceLink))
    journey_pattern = GeneratorTester(load_generator(db_target, ServiceJourneyPattern))
    transfer = GeneratorTester(
        chain(load_generator(db_target, Connection), load_generator(db_target, SiteConnection),
              load_generator(db_target, DefaultConnection)))
    stop_assignment = GeneratorTester(load_generator(db_target, PassengerStopAssignment))
    notice = GeneratorTester(load_generator(db_target, Notice))

    service_journey = GeneratorTester(load_generator(db_target, ServiceJourney))
    service_journey_interchange = GeneratorTester(load_generator(db_target, ServiceJourneyInterchange))

    service_calendar = GeneratorTester(load_generator(db_target, ServiceCalendar, 1))

    other_referenced_classes = [Codespace, DataSource, Authority, Operator, ValueSet,
                                TransportAdministrativeZone, ResponsibilitySet, StopPlace,
                                TopographicPlace, Direction, Line, FlexibleLine,
                                Network, DestinationDisplay, ScheduledStopPoint, TariffZone, ServiceLink,
                                ServiceJourneyPattern, Connection, SiteConnection, DefaultConnection,
                                PassengerStopAssignment, Notice, ServiceJourney, ServiceCalendar, VehicleType,
                                ServiceJourneyInterchange]

    other_referenced_objects = GeneratorTester(
        fetch_references_classes_generator(db_orig, db_target, other_referenced_classes))

    version = date.today().strftime("%Y%m%d")

    default_locale: LocaleStructure = project(list(all_locales)[0], LocaleStructure) if len(
        all_locales) > 0 else None
    if default_locale is not None and default_locale.languages is not None and len(
            default_locale.languages.language_usage) == 1:
        default_locale.default_language = default_locale.languages.language_usage[0].language

    publication_delivery = PublicationDelivery(
        version="ntx:1.1",
        publication_timestamp=XmlDateTime.now(),
        participant_ref=ParticipantRef(value=defaults["particpant_ref"]),
        description=MultilingualString(value=defaults["xml_description"]),
        data_objects=DataObjectsRelStructure(choice=[
            CompositeFrame(
                id="EU_PI_NETWORK_OFFER", version=version,
                type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK_OFFER', version_ref='1.0'),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_location_system="urn:ogc:def:crs:EPSG::4326",
                    default_system_of_units=SystemOfUnits.SI_METRES,
                    default_locale=default_locale
                    ),
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=codespace_ref_or_codespace.generator()) if codespace_ref_or_codespace.has_value() else None,
                frames=FramesRelStructure(
                    common_frame=[
                        ResourceFrame(
                            id="COMMON", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:COMMON', version_ref='1.0'),
                            data_sources=DataSourcesInFrameRelStructure(
                                data_source=data_source.generator()) if data_source.has_value() else None,
                            types_of_value=TypesOfValueInFrameRelStructure(
                                choice=value_set.generator()) if value_set.has_value() else None,
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=organisation_or_transport_organisation) if len(
                                organisation_or_transport_organisation) > 0 else None,
                            vehicle_types=VehicleTypesInFrameRelStructure(
                                transport_type_dummy_type_or_train_type=transport_type_dummy_type_or_train_type.generator()) if transport_type_dummy_type_or_train_type.has_value() else None,
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=responsibility_set.generator()) if responsibility_set.has_value() else None,
                            zones=ZonesInFrameRelStructure(
                                choice=transport_administrative_zone.generator()) if transport_administrative_zone.has_value() else None,
                            # brandings=BrandingsInFrameRelStructure(branding=load_generator(con, Branding)) # TODO: must be added to a ValueSet
                        ),

                        SiteFrame(
                            id="EU_PI_STOP", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_STOP', version_ref='1.0'),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=stop_place.generator()) if stop_place.has_value() else None,
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=topographic_place.generator()) if topographic_place.has_value() else None,
                        ),

                        ServiceFrame(
                            id="EU_PI_NETWORK", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK', version_ref='1.0'),
                            directions=DirectionsInFrameRelStructure(
                                direction=direction.generator()) if direction.has_value() else None,
                            lines=LinesInFrameRelStructure(line=line.generator()) if line.has_value() else None,
                            network=list(network.generator())[0] if network.has_value() else None,
                            # Warning; we must handle multiple stuff
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=destination_display.generator()) if destination_display.has_value() else None,
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=scheduled_stop_point.generator()) if scheduled_stop_point.has_value() else None,
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=service_link.generator()) if service_link.has_value() else None,
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                journey_pattern=journey_pattern.generator()) if journey_pattern.has_value() else None,
                            connections=TransfersInFrameRelStructure(
                                transfer=transfer.generator()) if transfer.has_value() else None,
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment_or_passenger_boarding_position_assignment=stop_assignment.generator()) if stop_assignment.has_value() else None,
                            notices=NoticesInFrameRelStructure(
                                notice=notice.generator()) if notice.has_value() else None,
                            tariff_zones=TariffZonesInFrameRelStructure(
                                tariff_zone=tariff_zone.generator()) if tariff_zone.has_value() else None,
                        ),
                        TimetableFrame(
                            id="EU_PI_TIMETABLE", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_TIMETABLE', version_ref='1.0'),
                            # content_validity_conditions=ValidityConditionsRelStructure(choice=availability_condition.generator()) if availability_condition.has_value() else None,
                            vehicle_journeys=JourneysInFrameRelStructure(
                                vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journey.generator()) if service_journey.has_value() else None,
                            journey_interchanges=JourneyInterchangesInFrameRelStructure(
                                service_journey_pattern_interchange_or_service_journey_interchange=service_journey_interchange.generator()) if service_journey_interchange.has_value() else None
                        ),
                        ServiceCalendarFrame(
                            id="EU_PI_CALENDAR", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_CALENDAR', version_ref='1.0'),
                            service_calendar=list(service_calendar.generator())[
                                0] if service_calendar.has_value() else None,
                            # Warning; we must handle multiple stuff
                        ),

                        GeneralFrame(
                            id="OTHER_REFERENCED", version=version,
                            members=GeneralFrameMembersRelStructure(
                                choice=other_referenced_objects.generator()) if other_referenced_objects.has_value() else None
                        )
                    ]
                )
            )
        ]))

    return publication_delivery

def epip_service_journey_interchange(db_read: Database, db_write: Database, generator_defaults: dict) -> Generator:
    print(sys._getframe().f_code.co_name)

    def query1(db_read: Database) -> Generator:
        # _load_generator = load_generator(db_read, InterchangeRule)
        # for interchange_rule in _load_generator:
        #     interchange_rule: InterchangeRule
        #     service_journey_interchange: ServiceJourneyInterchange = project(interchange_rule, ServiceJourneyInterchange)
        #     yield service_journey_interchange

        _load_generator = load_generator(db_read, JourneyMeeting)
        for journey_meeting in _load_generator:
            journey_meeting: JourneyMeeting
            service_journey_interchange: ServiceJourneyInterchange = project(journey_meeting, ServiceJourneyInterchange)
            yield service_journey_interchange

    write_generator(db_write, ServiceJourneyInterchange, query1(db_read))
