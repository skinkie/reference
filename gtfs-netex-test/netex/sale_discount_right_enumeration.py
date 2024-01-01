from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SaleDiscountRightEnumeration(Enum):
    TRAVEL_CARD = "travelCard"
    PAY_AS_YOU_GO_RIGHT = "payAsYouGoRight"
    STATUTORY_RIGHT = "statutoryRight"
    OTHER = "other"
