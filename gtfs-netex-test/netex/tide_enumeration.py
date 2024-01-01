from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TideEnumeration(Enum):
    HIGH_TIDE = "HighTide"
    LOW_TIDE = "LowTide"
    NEAP_TIDE = "NeapTide"
    ALL_TIDES = "AllTides"
