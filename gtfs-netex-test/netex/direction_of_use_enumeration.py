from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DirectionOfUseEnumeration(Enum):
    """
    Allowed values for direction of use.
    """
    UP = "up"
    DOWN = "down"
    BOTH = "both"
