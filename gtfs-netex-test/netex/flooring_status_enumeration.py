from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlooringStatusEnumeration(Enum):
    GOOD = "good"
    WORN = "worn"
    DISCOMFORTABLE = "discomfortable"
    HAZARDOUS = "hazardous"
    UNKNOWN = "unknown"
