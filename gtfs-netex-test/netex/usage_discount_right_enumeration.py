from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageDiscountRightEnumeration(Enum):
    """
    Allowed values for  USAGE DISCOUNT RIGHT enumeration +v1.1.
    """
    MILEAGE_POINTS = "mileagePoints"
    USAGE_REBATE = "usageRebate"
    OTHER = "other"
