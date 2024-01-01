from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameOperatorEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    PARTICIPATING = "participating"
    DIFFERENT = "different"
