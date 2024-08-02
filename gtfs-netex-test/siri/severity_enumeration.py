from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SeverityEnumeration(Enum):
    UNKNOWN = "unknown"
    VERY_SLIGHT = "verySlight"
    SLIGHT = "slight"
    NORMAL = "normal"
    SEVERE = "severe"
    VERY_SEVERE = "verySevere"
    NO_IMPACT = "noImpact"
    UNDEFINED = "undefined"
