import netex_monkeypatching
from netex import AvailabilityCondition, UicOperatingPeriod, OperatingDay, DayTypeAssignment, DayType, OperatingDayRef, \
    DayTypeRef, DayOfWeekEnumeration
from netexio.database import Database
from netexio.dbaccess import get_single, load_local
from refs import getRef
from utils import project

def datetime_weekday_to_dow(wd: int) -> DayOfWeekEnumeration:
    match wd:
        case 0:
            return DayOfWeekEnumeration.MONDAY
        case 1:
            return DayOfWeekEnumeration.TUESDAY
        case 2:
            return DayOfWeekEnumeration.WEDNESDAY
        case 3:
            return DayOfWeekEnumeration.THURSDAY
        case 4:
            return DayOfWeekEnumeration.FRIDAY
        case 5:
            return DayOfWeekEnumeration.SATURDAY
        case 6:
            return DayOfWeekEnumeration.SUNDAY

    return DayOfWeekEnumeration.NONE

def get_day_type_from_availability_condition(db_read: Database, availability_condition: AvailabilityCondition) -> tuple[
    DayType, list[DayTypeAssignment], list[OperatingDay], UicOperatingPeriod]:
    day_type = None
    day_type_assignments = []
    my_operating_days = []
    uic_operating_period = None

    if len(availability_condition.day_types.day_type_ref_or_day_type) == 1:
        if isinstance(availability_condition.day_types.day_type_ref_or_day_type[0], DayType):
            day_type = availability_condition.day_types.day_type_ref_or_day_type[0]
        elif isinstance(availability_condition.day_types.day_type_ref_or_day_type[0], DayTypeRef):
            day_type = load_local(db_read, DayType, limit=1, filter=availability_condition.day_types.day_type_ref_or_day_type[0].id, cursor=True)[0]
    else:
        day_type = project(availability_condition, DayType)

    if availability_condition.valid_day_bits is not None:
        uic_operating_period: UicOperatingPeriod = project(availability_condition, UicOperatingPeriod)
        day_type_assignment = project(availability_condition, DayTypeAssignment)
        day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date = getRef(
            uic_operating_period)
        day_type_assignments.append(day_type_assignment)

    elif availability_condition.operating_days is not None:
        for operating_day in availability_condition.operating_days.operating_day_ref_or_operating_day:
            if isinstance(operating_day, OperatingDayRef):
                operating_day_ref = operating_day
                operating_day = load_local(db_read, OperatingDay, limit=1, filter=operating_day.ref, cursor=True)[0]
            else:
                operating_day_ref = getRef(operating_day)

            my_operating_days.append(operating_day)
            day_type_assignment = project(operating_day, DayTypeAssignment)
            day_type_assignment.is_available = availability_condition.is_available
            day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date = operating_day_ref

            day_type_assignments.append(day_type_assignment)

    return (day_type, day_type_assignments, my_operating_days, uic_operating_period)
