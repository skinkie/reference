from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleLinkTypeEnumeration(Enum):
    HAIL_AND_RIDE = "hailAndRide"
    ON_DEMAND = "onDemand"
    FIXED = "fixed"
    OTHER = "other"
