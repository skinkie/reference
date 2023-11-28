from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleLinkTypeEnumeration(Enum):
    """
    Allowed values for Flexible LINK TYPE.
    """
    HAIL_AND_RIDE = "hailAndRide"
    ON_DEMAND = "onDemand"
    FIXED = "fixed"
    OTHER = "other"
