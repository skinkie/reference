from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ProgressRateEnumeration(Enum):
    NO_PROGRESS = "noProgress"
    SLOW_PROGRESS = "slowProgress"
    NORMAL_PROGRESS = "normalProgress"
    FAST_PROGRESS = "fastProgress"
    UNKNOWN = "unknown"
