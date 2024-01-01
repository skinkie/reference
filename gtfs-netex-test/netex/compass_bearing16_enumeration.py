from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CompassBearing16Enumeration(Enum):
    SW = "SW"
    SE = "SE"
    NW = "NW"
    NE = "NE"
    W = "W"
    E = "E"
    S = "S"
    N = "N"
