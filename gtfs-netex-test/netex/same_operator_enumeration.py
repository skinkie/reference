from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameOperatorEnumeration(Enum):
    """
    Allowed values for Operator ENTITLEMENT CONSTRAINT.
    """
    ANY = "any"
    SAME = "same"
    PARTICIPATING = "participating"
    DIFFERENT = "different"
