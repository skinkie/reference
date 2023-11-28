from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageChargingBasisEnumeration(Enum):
    """
    Allowed values for LUGGAGE CHARGING BASIS.
    """
    FREE = "free"
    CHARGED_BY_ITEM = "chargedByItem"
    CHARGED_BY_WEIGHT = "chargedByWeight"
    OTHER = "other"
