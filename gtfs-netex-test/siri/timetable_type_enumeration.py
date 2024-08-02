from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TimetableTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    SPECIAL = "special"
    EMERGENCY = "emergency"
    UNDEFINED_TIMETABLE_TYPE = "undefinedTimetableType"
