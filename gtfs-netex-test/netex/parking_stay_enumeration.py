from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingStayEnumeration(Enum):
    SHORT_STAY = "shortStay"
    MID_TERM = "midTerm"
    LONG_TERM = "longTerm"
    DROPOFF = "dropoff"
    UNLIMITED = "unlimited"
    OTHER = "other"
    ALL = "all"
