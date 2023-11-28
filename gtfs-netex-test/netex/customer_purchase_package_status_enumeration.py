from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CustomerPurchasePackageStatusEnumeration(Enum):
    """Allowed values for CUSTOMER PURCHASE PACKAGE  Status.

    +v1.1

    :cvar RESERVED: Reserved but not paid for.
    :cvar ORDERED: Purchased but not paid for.
    :cvar PAID_FOR: Paid for.
    :cvar UNUSED: Fulfilled but has not yet been used.
    :cvar ACTIVATED: Activated for use.
    :cvar PARTIALLY_USED: Partially used.
    :cvar USED: Fully used.
    :cvar ARCHIVED: Archived.
    :cvar OTHER: Other status.
    """
    RESERVED = "reserved"
    ORDERED = "ordered"
    PAID_FOR = "paidFor"
    UNUSED = "unused"
    ACTIVATED = "activated"
    PARTIALLY_USED = "partiallyUsed"
    USED = "used"
    ARCHIVED = "archived"
    OTHER = "other"
