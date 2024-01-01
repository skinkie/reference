from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AmountOfPriceUnitEnumeration(Enum):
    TRIP_CARNET = "tripCarnet"
    PASS_CARNET = "passCarnet"
    UNIT_COUPON = "unitCoupon"
    STORED_VALUE = "storedValue"
    OTHER = "other"
