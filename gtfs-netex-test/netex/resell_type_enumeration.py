from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResellTypeEnumeration(Enum):
    NONE = "none"
    PARTIAL = "partial"
    SLIDING_SCALE = "slidingScale"
    FULL = "full"
