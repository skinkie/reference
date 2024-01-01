from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingVisibilityEnumeration(Enum):
    UNMARKED = "unmarked"
    SIGNAGE_ONLY = "signageOnly"
    DEMARCATED = "demarcated"
    DOCKS = "docks"
    OTHER = "other"
