from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntitlementTypeEnumeration(Enum):
    NONE = "none"
    PURCHASE = "purchase"
    PURCHASE_AT_DISCOUNT = "purchaseAtDiscount"
    USE = "use"
    OTHER = "other"
