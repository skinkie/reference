from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneRuleApplicabilityEnumeration(Enum):
    """
    Allowed values for Zone Rule APplicability.
    """
    INSIDE = "inside"
    OUTSIDE = "outside"
