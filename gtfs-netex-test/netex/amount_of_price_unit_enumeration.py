from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AmountOfPriceUnitEnumeration(Enum):
    """
    Allowed values for AMOUNT OF PRICE UNIT enumeration +v1.1.
    """
    TRIP_CARNET = "tripCarnet"
    PASS_CARNET = "passCarnet"
    UNIT_COUPON = "unitCoupon"
    STORED_VALUE = "storedValue"
    OTHER = "other"
