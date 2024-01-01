from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameRouteEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    OPPOSITE_DIRECTION = "oppositeDirection"
    DIFFERENT = "different"
