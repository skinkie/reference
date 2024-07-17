# import sqlite3
import duckdb as sqlite3
import sys
import warnings
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from functools import partial
from itertools import chain
from multiprocessing import Pool
from typing import Generator, List, Dict

from xsdata.models.datatype import XmlDateTime, XmlDate

from callsprofile import CallsProfile
from netex import Line, ScheduledStopPoint, PassengerStopAssignment, Quay, StopPlace, AccessSpace, PosList, \
    ServiceJourneyPattern, TimeDemandType, ServiceJourney, AvailabilityCondition, CallsRelStructure, \
    StopPointInJourneyPattern, PointsInJourneyPatternRelStructure, TimetabledPassingTimesRelStructure, \
    UicOperatingPeriod, DayTypeAssignment, DayType, ValidityConditionsRelStructure, AvailabilityConditionRef, \
    ServiceCalendar, DayTypeRefsRelStructure, DayTypesRelStructure, OperatingPeriodsRelStructure, \
    DayTypeAssignmentsRelStructure, OperatingPeriodRef, RouteView

from netexio.dbaccess import load_generator, load_local, write_generator, write_objects, get_single, load_lxml_generator, \
    write_lxml_generator
from refs import getIndex, getRef, getId
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from transformers.projection import project_location_4326, project_polygon
from utils import project

EPIP_CLASSES = [ "Codespace", "StopPlace", "RoutePoint", "RouteLink", "Routes", "ScheduledStopPoint", "Operator", "VehicleType", "Line", "Direction", "DestinationDisplay", "ServiceJourney", "ServiceJourneyPattern", "PassengerStopAssignment", "Notice", "NoticeAssignment", "AvailabilityCondition" ]

def epip_line_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(line: Line):
        line.branding_ref = None
        line.type_of_service_ref = None
        line.type_of_product_category_ref = None
        return line

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, Line)
        for line in pool.imap_unordered(process, _load_generator, chunksize=100):
            yield line

    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        write_generator(write_con, Line, query(read_con), True)

def epip_line_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        lines: List[Line] = load_local(read_con, Line)
        for line in lines:
            line.branding_ref = None
            line.type_of_service_ref = None
            line.type_of_product_category_ref = None
        write_objects(write_con, lines, True, True)

def epip_scheduled_stop_point_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        ssp.stop_areas = None
        ssp.key_list = None
        ssp.extensions = None
        project_location_4326(ssp.location, generator_defaults)
        return ssp

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, ScheduledStopPoint)
        for ssp in pool.imap_unordered(partial(process, generator_defaults=generator_defaults), _load_generator, chunksize=100):
            yield ssp

    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        write_generator(write_con, ScheduledStopPoint, query(read_con), True)

def epip_scheduled_stop_point_memory(read_database: str, write_database: str, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
        for ssp in scheduled_stop_points:
            ssp: ScheduledStopPoint
            ssp.stop_areas = None
            if ssp.location is not None:
                project_location_4326(ssp.location, generator_defaults)
            else:
                print(f"ScheduledStopPoint {ssp.id} does not have a location.")

        write_objects(write_con, scheduled_stop_points, True, True)

def epip_site_frame_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)

    with sqlite3.connect(read_database) as read_con:
        stop_places: dict[str, StopPlace] = getIndex(load_local(read_con, StopPlace))

        # Resolving a quay is very expensive. Either in the database it should be stored independently, or an index should be made available.
        quays: dict[str, Quay] = getIndex([quay for quay in chain(*[stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay for stop_place in stop_places.values() if stop_place.quays is not None]) if isinstance(quay, Quay)])

        with sqlite3.connect(write_database) as write_con:
            refs = set([])

            stop_assignments: List[PassengerStopAssignment] = load_local(read_con, PassengerStopAssignment)
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
                write_objects(write_con, retain_stop_assignments, True, True)

            stop_places: List[StopPlace] = load_local(read_con, StopPlace)
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

                                project_polygon(quay.polygon_or_multi_surface, generator_defaults, 'urn:ogc:def:crs:EPSG::4326')

                            project_location_4326(quay.centroid.location, generator_defaults)

                project_location_4326(stop_place.centroid.location, generator_defaults)
                retained_stop_places.append(stop_place)

            write_objects(write_con, retained_stop_places, True, True)

def epip_timetabled_passing_times_memory(read_database, write_database, generator_defaults, dynamics=[]):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            # TODO: Maybe do this on the fly, per servicejourney?
            service_journey_patterns: List[ServiceJourneyPattern] = load_local(read_con, ServiceJourneyPattern)
            time_demand_types = load_local(read_con, TimeDemandType)
            service_journeys = load_local(read_con, ServiceJourney)

            timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

            # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
            timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)
            time_demand_types = None

            availability_conditions = load_local(read_con, AvailabilityCondition)
            servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
            service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
            write_objects(write_con, [service_calendar], True, False)

            for sj in service_journeys:
                sj: ServiceJourney
                sj.validity_conditions_or_valid_between = None
                sj.key_list = None
                sj.private_code = None

                # TODO: Benchmark
                any(map(lambda x: x(sj), dynamics))
                # for dynamic in dynamics:
                #     dynamic(sj)

            write_objects(write_con, service_journeys, True, False)

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
        ac: ValidityConditionsRelStructure
        for a in ac.choice:
            if isinstance(a, AvailabilityConditionRef):
                acs.append(availability_conditions[a.ref])
            elif isinstance(a, AvailabilityCondition):
                acs.append(a)
            else:
                warnings.warn(f"Unhandled ValidityCondition in {service_journey.id}")

    # TODO: this will fail in extreme cases
    day_type_id = acs[0].id.replace('AvailabilityCondition', 'DayType')

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
    from_date = min([uic.from_operating_day_ref_or_from_date.to_datetime() for uic in uic_operating_periods])
    to_date = max([uic.to_operating_day_ref_or_to_date.to_datetime() for uic in uic_operating_periods])

    return ServiceCalendar(id=getId(ServiceCalendar, generator_defaults['codespace'], "ServiceCalendar"),
                           version=generator_defaults['version'],
                           from_date=XmlDate.from_date(from_date.date()), to_date=XmlDate.from_date(to_date.date()),
                           day_types=DayTypesRelStructure(day_type_ref_or_day_type=list(day_types.values())),
                           operating_periods=OperatingPeriodsRelStructure(uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period=uic_operating_periods),
                           day_type_assignments=DayTypeAssignmentsRelStructure(day_type_assignment=day_type_assignments))

def epip_service_journey_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)
    sjps: Dict[str, ServiceJourneyPattern] = {}
    availability_conditions: Dict[str, AvailabilityCondition] = {}
    day_types: Dict[str, DayType] = {}
    uic_operating_periods: List[UicOperatingPeriod] = []
    day_type_assignments: List[DayTypeAssignment] = []

    def process(sj: ServiceJourney, read_database, write_database, generator_defaults: dict):
        sj: ServiceJourney

        # Prototype, just: TimeDemandType -> PassingTimes
        with sqlite3.connect(read_database) as read_con:
            if sj.passing_times:
                pass

            elif sj.calls:
                if sj.journey_pattern_ref:
                    service_journey_pattern: ServiceJourneyPattern = get_single(read_con, ServiceJourneyPattern,
                                                                                sj.journey_pattern_ref.ref,
                                                                                sj.journey_pattern_ref.version)
                else:
                    service_journey_pattern = service_journey_pattern_from_calls(sj, generator_defaults)
                    sj.journey_pattern_ref = getRef(service_journey_pattern)
                    sjps[service_journey_pattern.id] = service_journey_pattern

                sj.passing_times = TimetabledPassingTimesRelStructure(timetabled_passing_time=TimetablePassingTimesProfile.getTimetabledPassingtimesFromCalls(sj, service_journey_pattern))

            elif sj.time_demand_type_ref:
                service_journey_pattern: ServiceJourneyPattern = get_single(read_con, ServiceJourneyPattern,
                                                                            sj.journey_pattern_ref.ref,
                                                                            sj.journey_pattern_ref.version)
                time_demand_type: TimeDemandType = get_single(read_con, TimeDemandType, sj.time_demand_type_ref.ref,
                                                              sj.time_demand_type_ref.version)
                CallsProfile.getPassingTimesFromTimeDemandType(sj, service_journey_pattern, time_demand_type)

        service_journey_ac_to_day_type(sj, availability_conditions, day_types, uic_operating_periods, day_type_assignments)

        # TODO: AvailabilityCondition -> Uic

        sj.validity_conditions_or_valid_between = None
        sj.key_list = None
        sj.private_code = None
        sj.train_numbers = None
        sj.extensions = None
        sj.notice_assignments = None
        sj.calls = None
        return sj

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, ServiceJourney)
        for sj in _load_generator:
            yield process(sj, read_database, write_database, generator_defaults)
        # for sj in pool.imap_unordered(partial(process, read_database=read_database, write_database=write_database, generator_defaults=generator_defaults), _load_generator, chunksize=100):
        #     yield sj

    with sqlite3.connect(read_database) as read_con:
        availability_conditions = getIndex(load_local(read_con, AvailabilityCondition))

    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        write_generator(write_con, ServiceJourney, query(read_con), True)
        write_objects(write_con, list(sjps.values()), True, True)

        service_calendar = get_service_calendar(day_types, uic_operating_periods, day_type_assignments, generator_defaults)

        write_objects(write_con, [service_calendar], True, True)

        # availability_conditions = load_local(read_con, AvailabilityCondition)
        # servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
        # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys,
        #                                                                                availability_conditions)
        # write_objects(write_con, [service_calendar], True, False)

        # timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

            # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
            # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

            # availability_conditions = load_local(read_con, AvailabilityCondition)
            # servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
            # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
            # write_objects(write_con, [service_calendar], True, False)

def epip_remove_keylist_extensions(read_database: str, write_database: str, generator_defaults: dict):
    def process(tree, keys: List):
        for key in keys:
            for element in tree.iterfind(key):
                element.getparent().remove(element)
        return tree

    def query1(read_con) -> Generator:
        _load_generator = load_generator(read_con, StopPlace)
        for tree in load_lxml_generator(write_con, StopPlace):
            yield process(tree, [".//{http://www.netex.org.uk/netex}keyList", ".//{http://www.netex.org.uk/netex}Extensions"])


    def query2(read_con) -> Generator:
        _load_generator = load_generator(read_con, ScheduledStopPoint)
        for tree in load_lxml_generator(write_con, ScheduledStopPoint):
            yield process(tree, [".//{http://www.netex.org.uk/netex}keyList", ".//{http://www.netex.org.uk/netex}Extensions"])

    def query3(read_con) -> Generator:
        _load_generator = load_generator(read_con, ServiceJourneyPattern)
        for tree in load_lxml_generator(write_con, ServiceJourneyPattern):
            yield process(tree, [".//{http://www.netex.org.uk/netex}keyList", ".//{http://www.netex.org.uk/netex}Extensions"])

    def query4(read_con) -> Generator:
        _load_generator = load_generator(read_con, ServiceJourney)
        for tree in load_lxml_generator(write_con, ServiceJourney):
            yield process(tree, [".//{http://www.netex.org.uk/netex}keyList", ".//{http://www.netex.org.uk/netex}Extensions"])

    # TODO: Make the database access pattern generic.
    with sqlite3.connect(write_database) as write_con:
        if write_database == read_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        write_lxml_generator(write_con, StopPlace, query1(read_con))
        write_lxml_generator(write_con, ScheduledStopPoint, query2(read_con))
        write_lxml_generator(write_con, ServiceJourneyPattern, query3(read_con))
        write_lxml_generator(write_con, ServiceJourney, query4(read_con))