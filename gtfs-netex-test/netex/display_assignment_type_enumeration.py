from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DisplayAssignmentTypeEnumeration(Enum):
    """
    Allowed values for Display Assignment Type.
    """
    ARRIVALS = "arrivals"
    DEPARTURES = "departures"
    ALL = "all"
