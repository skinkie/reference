from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DisplayAssignmentTypeEnumeration(Enum):
    ARRIVALS = "arrivals"
    DEPARTURES = "departures"
    ALL = "all"
