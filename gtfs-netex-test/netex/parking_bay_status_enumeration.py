from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingBayStatusEnumeration(Enum):
    """
    Allowed values for PARKING BAY STATUS.
    """
    AVAILABLE = "available"
    IN_USE = "inUse"
    OUT_OF_SERVICE = "outOfService"
    RESERVED = "reserved"
    UNKNOWN = "unknown"
