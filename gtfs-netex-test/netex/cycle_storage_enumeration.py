from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CycleStorageEnumeration(Enum):
    RACKS = "racks"
    DOCKS = "docks"
    BARS = "bars"
    RAILINGS = "railings"
    CYCLE_SCHEME = "cycleScheme"
    LOCKERS = "lockers"
    FREESTANDING = "freestanding"
    OTHER = "other"
