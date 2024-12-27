import sys
import warnings
from typing import Generator, List, T

from xsdata.models.datatype import XmlDate

from callsprofile import CallsProfile
from gtfsprofile import GtfsProfile
from netex import Line, Branding, Operator, Authority, ResponsibilitySet, StakeholderRoleTypeEnumeration, \
    ServiceJourney, LineRef, StopPlace, PassengerStopAssignment, ScheduledStopPoint, TemplateServiceJourney, \
    ServiceJourneyPattern, TimeDemandType, RouteView, RouteRef, Route, ValidityConditionsRelStructure, \
    AvailabilityCondition, AvailabilityConditionRef, DayType, DayTypeAssignment, OperatingPeriod, ServiceCalendar, \
    DayTypesRelStructure, OperatingPeriodRef, UicOperatingPeriodRef, OperatingDay, DayTypeRef, \
    OperatingDaysRelStructure, OperatingDayRefStructure, UicOperatingPeriod, OperatingDayRef, \
    PropertiesOfDayRelStructure, PropertyOfDay
from netexio.database import Database
from netexio.dbaccess import load_generator, load_local, write_objects, get_single, write_generator, copy_table
from refs import getRef, getIndex, getIndexByGroup, getId
from utils import project, chain

import netex_monkeypatching

GTFS_CLASSES = [ "Codespace", "StopPlace", "ScheduledStopPoint", "Authority", "Operator", "Line", "DestinationDisplay",
                 "ServiceJourney", "ServiceJourneyPattern", "PassengerStopAssignment", "AvailabilityCondition",
                 "DayTypeAssignment", "UicOperatingPeriod", "TemplateServiceJourney", "Branding",
                 "InterchangeRule", "ServiceJourneyInterchange, JourneyMeeting"]

def gtfs_operator_line_memory(db_read: Database, db_write: Database, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    lines: list[Line] = load_local(db_read, Line)
    operators_local: list[Operator] = load_local(db_read, Operator)

    operators: dict[str, Operator] = {}
    for line in lines:
        # GTFS only has the concept agency (operator) hence all variants will become OperatorRef.
        if line.branding_ref is not None:
            branding: Branding = get_single(db_read, Branding, line.branding_ref.ref, line.branding_ref.version)
            operator: Operator = project(branding, Operator)
            operators[operator.id] = operator
            line.operator_ref = getRef(operator)

        elif line.operator_ref is not None:
            if line.operator_ref.ref not in operators:
                operator: Operator = get_single(db_read, Operator, line.operator_ref.ref, line.operator_ref.version)
                operators[operator.id] = operator
                line.operator_ref = getRef(operator)

        elif line.authority_ref is not None:
            authority: Authority = get_single(db_read, Authority, line.authority_ref.ref, line.authority_ref.version)
            operator: Operator = project(authority, Operator)
            operators[operator.id] = operator
            line.operator_ref = getRef(operator)

        elif line.responsibility_set_ref_attribute is not None:
            # TODO: ResponsibilitySet to Operator/Authority should be a separate function
            responsibility_set: ResponsibilitySet = get_single(db_read, ResponsibilitySet, line.responsibility_set_ref_attribute)
            if responsibility_set is not None and responsibility_set.roles is not None:
                for role_assignment in responsibility_set.roles.responsibility_role_assignment:
                    if StakeholderRoleTypeEnumeration.OPERATION in role_assignment.stakeholder_role_type or StakeholderRoleTypeEnumeration.OPERATION_1 in role_assignment.stakeholder_role_type:
                        operator: Operator = get_single(db_read, db_read.get_class_by_name(role_assignment.responsible_organisation_ref.name_of_ref_class), role_assignment.responsible_organisation_ref.ref, role_assignment.responsible_organisation_ref.version)
                        operators[operator.id] = operator
                        line.operator_ref = getRef(operator)

        if line.operator_ref is None:
            if len(operators_local) == 1:
                operator: Operator = operators_local[0]
                operators[operator.id] = operator
                line.operator_ref = getRef(operator)

            else:
                # Is there any ServiceJourney -> OperatorRef relationship?
                # TODO: Now we would like to filter on a property such as LineRef, but that may obviously be unavailable...
                # TODO: Implement the reference chain by the reference table, so it finds the object of interest, by joins (inna-search)
                # TODO: Iff multiple OperatorRefs are pointing to the same LineRef, the LineRef must be duplicated for GTFS export.
                db_read.logger.info("Operator not found for {line}. Implement Innasearch.")
                pass

        line.authority_ref = None
        line.responsibility_set_ref_attribute = None
        line.branding_ref = None

        if line.operator_ref is None:
            db_read.logger.error(f"Line {line.id} does not have an operator_ref assigned.")

    write_objects(db_write, list(operators.values()), True, True)
    write_objects(db_write, lines, True, True)

def gtfs_calls_generator(db_read: Database, db_write: Database, generator_defaults: dict):
    def query_sj(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ServiceJourney)
        for sj in _load_generator:
            sj: ServiceJourney
            if sj.calls:
                yield sj
            else:
                sjp: ServiceJourneyPattern = get_single(db_read, ServiceJourneyPattern, sj.journey_pattern_ref.ref, cursor=True)
                if sjp is None:
                    db_read.logger.error("No SJP")

                else:
                    # TODO: very costly to do it here for every ServiceJourneyPattern
                    if sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view is None:
                        if sjp.route_ref_or_route_view is not None:
                            if isinstance(sjp.route_ref_or_route_view, RouteView):
                                sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view = sjp.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view
                            elif isinstance(sjp.route_ref_or_route_view, RouteRef):
                                sj.route_ref = sjp.route_ref_or_route_view
                                route: Route = get_single(db_read, Route, sjp.route_ref_or_route_view.ref, cursor=True)
                                sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view = route.line_ref

                    if sj.passing_times:
                        CallsProfile.getCallsFromTimetabledPassingTimes(sj, sjp)
                        yield sj

                    elif sj.time_demand_type_ref:
                        tdt: TimeDemandType = get_single(db_read, TimeDemandType, sj.time_demand_type_ref.ref, cursor=True)
                        CallsProfile.getCallsFromTimeDemandType(sj, sjp, tdt)
                        yield sj

                    else:
                        db_read.logger.error("Unimplemented method to calls")


    write_generator(db_write, ServiceJourney, query_sj(db_read))

    def query_tsj(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, TemplateServiceJourney)
        for tsj in _load_generator:
            tsj: TemplateServiceJourney
            if tsj.calls:
                pass
            else:
                sjp: ServiceJourneyPattern = get_single(db_read, ServiceJourneyPattern, tsj.journey_pattern_ref.ref, cursor=True)
                if sjp is None:
                    db_read.logger.error("No SJP")

                elif tsj.passing_times:
                    CallsProfile.getCallsFromTimetabledPassingTimes(tsj, sjp)
                    yield tsj

                elif tsj.time_demand_type_ref:
                    tdt: TimeDemandType = get_single(db_read, TimeDemandType, sj.time_demand_type_ref.ref, cursor=True)
                    CallsProfile.getCallsFromTimeDemandType(tsj, sjp, tdt)
                    yield tsj

                else:
                    db_read.logger.error("Unimplemented method to calls")


    write_generator(db_write, TemplateServiceJourney, query_tsj(db_read))

def day_type_assignment_to_ac(day_type_assignment: DayTypeAssignment, day_type: DayType, ops: dict[str, OperatingPeriod | UicOperatingPeriod], ods: dict[str, OperatingDay]):
    ac: AvailabilityCondition = project(day_type_assignment, AvailabilityCondition)
    ac.is_available = day_type_assignment.is_available
    ac.day_types = DayTypesRelStructure(day_type_ref_or_day_type=[getRef(day_type)])

    # Most specific class first
    if isinstance(day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date, UicOperatingPeriodRef) or (isinstance(day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date, OperatingPeriodRef) or day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date.name_of_ref_class == 'UicOperatingPeriod'):
        uic_operating_period_ref = day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date
        uic_operating_period: UicOperatingPeriod = ops[uic_operating_period_ref.ref]

        if isinstance(uic_operating_period.from_operating_day_ref_or_from_date, OperatingDayRefStructure):
            od: OperatingDay = ods[uic_operating_period.from_operating_day_ref_or_from_date.ref]
            ac.from_date = od.calendar_date.to_datetime()
        else:
            ac.from_date = uic_operating_period.from_operating_day_ref_or_from_date

        if isinstance(uic_operating_period.to_operating_day_ref_or_to_date, OperatingDayRefStructure):
            od: OperatingDay = ods[uic_operating_period.to_operating_day_ref_or_to_date.ref]
            ac.to_date = od.calendar_date.to_datetime()
        else:
            ac.to_date = uic_operating_period.to_operating_day_ref_or_to_date

        ac.valid_day_bits = uic_operating_period.valid_day_bits

        if len(uic_operating_period.days_of_week) > 0:
            day_type_derived: DayType = project(day_type, DayType)
            day_type_derived.id = ac.id.replace(':AvailabilityCondition:', ':DayType:') + '_1'
            day_type_derived.properties = PropertiesOfDayRelStructure(property_of_day=[PropertyOfDay(days_of_week=uic_operating_period.days_of_week)])

            ac.day_types = DayTypesRelStructure(day_type_ref_or_day_type=[day_type_derived])

    elif isinstance(day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date, OperatingPeriodRef):
        operating_period_ref = day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date
        operating_period: OperatingPeriod = ops[operating_period_ref.ref]

        if isinstance(operating_period.from_operating_day_ref_or_from_date, OperatingDayRefStructure):
            od: OperatingDay = ods[operating_period.from_operating_day_ref_or_from_date.ref]
            ac.from_date = od.calendar_date.to_datetime()
        else:
            ac.from_date = operating_period.from_operating_day_ref_or_from_date

        if isinstance(operating_period.to_operating_day_ref_or_to_date, OperatingDayRefStructure):
            od: OperatingDay = ods[operating_period.to_operating_day_ref_or_to_date.ref]
            ac.to_date = od.calendar_date.to_datetime()
        else:
            ac.to_date = operating_period.to_operating_day_ref_or_to_date

    elif isinstance(day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date, OperatingDayRef):
        operating_day_ref = day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date
        ac.operating_days = OperatingDaysRelStructure(operating_day_ref_or_operating_day=[ods[operating_day_ref.ref]])

    elif isinstance(day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date, XmlDate):
        xml_date = day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date
        ac.operating_days = OperatingDaysRelStructure(operating_day_ref_or_operating_day=[OperatingDay(id=day_type.id.replace('DayType', 'OperatingDay') + '_' + str(xml_date), calendar_date=xml_date)])

    return ac

def service_calendar_to_availability_conditions(service_calendar: ServiceCalendar) -> Generator[AvailabilityCondition, None, None]:
    dtas = getIndexByGroup(service_calendar.day_type_assignments.day_type_assignment, 'day_type_ref') if service_calendar.day_type_assignments else {}
    ops = getIndex(service_calendar.operating_periods.uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period) if service_calendar.operating_periods else {} # TODO: This does not differentiate
    ods = getIndex(service_calendar.operating_days.operating_day_ref_or_operating_day) if service_calendar.operating_days else {}

    for day_type in service_calendar.day_types.day_type_ref_or_day_type:
        day_type_ref = getRef(day_type) if isinstance(day_type, DayType) else day_type

        for dta in dtas.get(day_type_ref, []):
            ac = day_type_assignment_to_ac(dta, day_type, ops, ods)
            yield ac, day_type_ref

def apply_availability_conditions_via_day_type_ref(db_read: Database, db_write: Database):
    def query_sc(mapping: dict):
        for service_calendar in load_generator(db_read, ServiceCalendar):
            for ac, day_type_ref in service_calendar_to_availability_conditions(service_calendar):
                if day_type_ref in mapping:
                    mapping[day_type_ref].append(getRef(ac))
                else:
                    mapping[day_type_ref] = [getRef(ac)]

                yield ac

    def query_sj(db_read: Database, mapping: dict, clazz: T) -> Generator:
        for service_journey in load_generator(db_read, clazz):
            service_journey: clazz
            if service_journey.day_types:
                for day_type_ref in service_journey.day_types.day_type_ref:
                    if day_type_ref in mapping:
                        if service_journey.validity_conditions_or_valid_between is None:
                            service_journey.validity_conditions_or_valid_between = ValidityConditionsRelStructure(choice=mapping[day_type_ref])
                        elif isinstance(service_journey.validity_conditions_or_valid_between, ValidityConditionsRelStructure):
                            service_journey.validity_conditions_or_valid_between.choice += mapping[day_type_ref]
            yield service_journey



    #with Database("/tmp/fake-mem.duckdb", read_only=False) as db_mem:
    mapping = {}

    copy_table(db_read, db_write, [AvailabilityCondition])
    write_generator(db_write, AvailabilityCondition, query_sc(mapping))
    # The point is here that we now "normalise" everything to availability conditions, but this isn't the target format yet.

    write_generator(db_write, DayType, load_generator(db_read, DayType, embedding=True))
    write_generator(db_write, ServiceJourney, query_sj(db_read, mapping, ServiceJourney))
    write_generator(db_write, TemplateServiceJourney, query_sj(db_read, mapping, TemplateServiceJourney))


def gtfs_calendar_generator(db_read: Database, db_write: Database, generator_defaults: dict):
    # This functions purpose is to transform calendars from NeTEx in such way it can be referenced by GTFS.
    # GTFS only has a validity on a Trip, hence the list of calendars is limited by the validity structure
    # referenced from SericeJourney and TemplateServiceJourney.
    # Given that we don't know how the structure looks like, it may be an AvailabilityCondition or a DayType
    # and further references thereof we take the following algorithm:
    #
    # Input:
    # 1. The combination of DayType + AvailabilityCondition(s) will form the unique service_id (extremely complex case where availabilitycondition or validbetween overrides the DayType)
    # 2. All pair ids will be collected, (de)normalisation is not an issue
    #
    # Output for GTFS:
    # 0. Our intermediate representation of calender.txt, calendar_dates.txt are two AvailabilityConditions (inclusive, and exclusive) and a separate one with a DayOfWeek.
    #    a GTFS service_id may be recovered from PrivateCode.
    # 1. If a DayType (DayOfWeek) has been provided, this will form a unique calendar.txt entry (mo-tue-wed-thu-fri-sat-sun)
    # 2. If both inclusive and exclusive are provided, we assume that the positive bits are the only entries that actually matter,
    #    we can warn for ambiguity, with respect to DayType not being coherent or both inclusive as exclusive values for the same date.
    #
    # ServiceCalendar to AvailabilityConditions

    def query_sj(db_read: Database) -> Generator:
        # DayType 1:N DayTypeAssignment 1:1 OperatingPeriodRef
        dts = load_local(db_read, DayType, embedding=True)
        dta = load_local(db_read, DayTypeAssignment, embedding=True)
        ops = load_local(db_read, OperatingPeriod, embedding=True)

        # N AvailabilityCondition
        avc = load_local(db_read, AvailabilityCondition, embedding=True)

        _load_generator = chain(load_generator(db_read, ServiceJourney), load_generator(db_read, TemplateServiceJourney))
        vcs: set[str] = set()
        day_type_refs: set[str] = set()

        for sj in _load_generator:
            sj: ServiceJourney
            if isinstance(sj.validity_conditions_or_valid_between, ValidityConditionsRelStructure):
                for vc in sj.validity_conditions_or_valid_between.choice:
                    if isinstance(vc, AvailabilityCondition):
                        vcs.add(vc.id)
                    elif isinstance(vc, AvailabilityConditionRef):
                        vcs.add(vc.ref)
                    else:
                        warnings.warn("Unimplemented other validity condition on ServiceJourney") # TODO: Only report once

            if sj.day_types is not None:
                for day_type_ref in sj.day_types.day_type_ref:
                    day_type_refs.add(day_type_ref.ref)

