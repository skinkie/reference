from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HandrailEnumeration(Enum):
    NONE = "none"
    ONE_SIDE = "oneSide"
    BOTH_SIDES = "bothSides"
