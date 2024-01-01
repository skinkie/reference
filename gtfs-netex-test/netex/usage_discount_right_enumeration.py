from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class UsageDiscountRightEnumeration(Enum):
    MILEAGE_POINTS = "mileagePoints"
    USAGE_REBATE = "usageRebate"
    OTHER = "other"
