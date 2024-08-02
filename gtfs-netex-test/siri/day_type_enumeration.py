from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DayTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    WEEKDAYS = "weekdays"
    WEEKENDS = "weekends"
    HOLIDAY = "holiday"
    PUBLIC_HOLIDAY = "publicHoliday"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    FEDERAL_HOLIDAY = "federalHoliday"
    REGIONAL_HOLIDAY = "regionalHoliday"
    NATIONAL_HOLIDAY = "nationalHoliday"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    SCHOOL_DAYS = "schoolDays"
    EVERY_DAY = "everyDay"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
