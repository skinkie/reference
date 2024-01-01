from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameJourneyEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    SIMILAR = "similar"
    DIFFERENT = "different"
