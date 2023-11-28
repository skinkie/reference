from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PathDirectionEnumeration(Enum):
    """
    Allowed values for flow direction.
    """
    ONE_WAY = "oneWay"
    TWO_WAY = "twoWay"
