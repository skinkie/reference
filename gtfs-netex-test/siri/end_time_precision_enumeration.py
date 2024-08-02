from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EndTimePrecisionEnumeration(Enum):
    DAY = "day"
    HOUR = "hour"
    SECOND = "second"
    MILLI_SECOND = "milliSecond"
