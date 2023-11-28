from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TaxCategoryEnumeration(Enum):
    """
    Allowed values for Tax categories +v1.1.
    """
    EXEMPT = "exempt"
    GENERAL = "general"
    TRANSPORTATION = "transportation"
    PARKING = "parking"
    FOOD = "food"
    ALCOHOLIC_BEVERAGE = "alcoholicBeverage"
    OTHER = "other"
