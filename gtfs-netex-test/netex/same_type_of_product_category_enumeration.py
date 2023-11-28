from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfProductCategoryEnumeration(Enum):
    """
    Allowed values for Type of Product category ENTITLEMENT CONSTRAINT.
    """
    ANY = "any"
    SAME = "same"
    SAME_OR_EQUIVALENT = "sameOrEquivalent"
    DIFFERENT = "different"
