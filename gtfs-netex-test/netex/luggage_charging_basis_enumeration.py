from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageChargingBasisEnumeration(Enum):
    FREE = "free"
    CHARGED_BY_ITEM = "chargedByItem"
    CHARGED_BY_WEIGHT = "chargedByWeight"
    OTHER = "other"
