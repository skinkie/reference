from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DiscountBasisEnumeration(Enum):
    """
    Allowed values for DiscountBasis.
    """
    NONE = "none"
    FREE = "free"
    DISCOUNT = "discount"
