from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SuitableEnumeration(Enum):
    """
    Allowed values for a SUITABILITY.
    """
    SUITABLE = "suitable"
    NOT_SUITABLE = "notSuitable"
