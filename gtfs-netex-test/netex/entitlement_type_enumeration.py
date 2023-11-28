from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntitlementTypeEnumeration(Enum):
    """
    Allowed values for ENTITLEMENT TYPE Type.
    """
    NONE = "none"
    PURCHASE = "purchase"
    PURCHASE_AT_DISCOUNT = "purchaseAtDiscount"
    USE = "use"
    OTHER = "other"
