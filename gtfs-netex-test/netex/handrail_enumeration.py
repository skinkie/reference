from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HandrailEnumeration(Enum):
    """
    Allowed values for Sides of handrail.
    """
    NONE = "none"
    ONE_SIDE = "oneSide"
    BOTH_SIDES = "bothSides"
