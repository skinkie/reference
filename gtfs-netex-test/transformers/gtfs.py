import sys
from typing import Generator

from callsprofile import CallsProfile
from gtfsprofile import GtfsProfile
from netex import Line, Branding, Operator, Authority, ResponsibilitySet, StakeholderRoleTypeEnumeration, \
    ServiceJourney, LineRef, StopPlace, PassengerStopAssignment, ScheduledStopPoint, TemplateServiceJourney, \
    ServiceJourneyPattern, TimeDemandType, RouteView, RouteRef, Route
from netexio.database import Database
from netexio.dbaccess import load_generator, load_local, write_objects, get_single, write_generator
from refs import getRef, getIndex
from utils import project

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
            if operator.id not in operators:
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
            for role_assignment in responsibility_set.roles.responsibility_role_assignment:
                if StakeholderRoleTypeEnumeration.OPERATION in role_assignment.stakeholder_role_type or StakeholderRoleTypeEnumeration.OPERATION_1 in role_assignment.stakeholder_role_type:
                    operator: Operator = get_single(db_read, getattr(sys.modules['netex'], role_assignment.responsible_organisation_ref.name_of_ref_class), role_assignment.responsible_organisation_ref.ref, role_assignment.responsible_organisation_ref.version)
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
