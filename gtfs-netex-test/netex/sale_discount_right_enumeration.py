from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SaleDiscountRightEnumeration(Enum):
    """
    Allowed values for  SDALE DISCOUNT RIGHT enumeration +v1.1.
    """
    TRAVEL_CARD = "travelCard"
    PAY_AS_YOU_GO_RIGHT = "payAsYouGoRight"
    STATUTORY_RIGHT = "statutoryRight"
    OTHER = "other"
