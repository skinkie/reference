from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScopingMethodEnumeration(Enum):
    EXPLICIT_STOPS = "explicitStops"
    IMPLICIT_SPATIAL_PROJECTION = "implicitSpatialProjection"
    EXPLICIT_PERIPHERY_STOPS = "explicitPeripheryStops"
    OTHER = "other"
