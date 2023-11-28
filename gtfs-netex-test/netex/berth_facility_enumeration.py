from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BerthFacilityEnumeration(Enum):
    """Allowed values for Berth Facility:"""
    UPPER = "upper"
    LOWER = "lower"
    BOTH = "both"
