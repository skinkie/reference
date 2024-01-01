from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SurfaceTypeEnumeration(Enum):
    ASPHALT = "asphalt"
    BRICKS = "bricks"
    COBBLES = "cobbles"
    EARTH = "earth"
    GRASS = "grass"
    LOOSE_SURFACE = "looseSurface"
    PAVING_STONES = "pavingStones"
    ROUGH_SURFACE = "roughSurface"
    SMOOTH = "smooth"
    OTHER = "other"
