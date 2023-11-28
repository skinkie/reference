from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageAllowanceTypeEnumeration(Enum):
    """
    Allowed values for LUGGAGE ALLOWANCE TYPE.
    """
    NONE = "none"
    SINGLE_BAG = "singleBag"
    LIMITED = "limited"
    UNLIMITED = "unlimited"
