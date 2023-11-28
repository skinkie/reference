from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameRouteEnumeration(Enum):
    """
    Allowed values for Route ENTITLEMENT CONSTRAINT.
    """
    ANY = "any"
    SAME = "same"
    OPPOSITE_DIRECTION = "oppositeDirection"
    DIFFERENT = "different"
