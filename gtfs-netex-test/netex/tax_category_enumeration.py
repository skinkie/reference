from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TaxCategoryEnumeration(Enum):
    EXEMPT = "exempt"
    GENERAL = "general"
    TRANSPORTATION = "transportation"
    PARKING = "parking"
    FOOD = "food"
    ALCOHOLIC_BEVERAGE = "alcoholicBeverage"
    OTHER = "other"
