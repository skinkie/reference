from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DirectionTypeEnumeration(Enum):
    """
    Allowed values for DIRECTION.
    """
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anticlockwise"
