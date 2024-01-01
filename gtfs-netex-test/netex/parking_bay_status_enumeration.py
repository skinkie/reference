from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingBayStatusEnumeration(Enum):
    AVAILABLE = "available"
    IN_USE = "inUse"
    OUT_OF_SERVICE = "outOfService"
    RESERVED = "reserved"
    UNKNOWN = "unknown"
