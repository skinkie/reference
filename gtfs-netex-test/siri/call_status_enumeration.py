from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CallStatusEnumeration(Enum):
    ON_TIME = "onTime"
    EARLY = "early"
    DELAYED = "delayed"
    CANCELLED = "cancelled"
    ARRIVED = "arrived"
    DEPARTED = "departed"
    MISSED = "missed"
    NO_REPORT = "noReport"
    NOT_EXPECTED = "notExpected"
