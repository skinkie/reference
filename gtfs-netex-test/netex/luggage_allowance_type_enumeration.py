from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageAllowanceTypeEnumeration(Enum):
    NONE = "none"
    SINGLE_BAG = "singleBag"
    LIMITED = "limited"
    UNLIMITED = "unlimited"
