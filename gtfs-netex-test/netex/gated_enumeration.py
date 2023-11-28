from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GatedEnumeration(Enum):
    """
    Allowed values for gated.
    """
    GATED_AREA = "gatedArea"
    OPEN_AREA = "openArea"
    UNKNOWN = "unknown"
