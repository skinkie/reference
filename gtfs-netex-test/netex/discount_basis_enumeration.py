from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DiscountBasisEnumeration(Enum):
    NONE = "none"
    FREE = "free"
    DISCOUNT = "discount"
