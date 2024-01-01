from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BerthFacilityEnumeration(Enum):
    UPPER = "upper"
    LOWER = "lower"
    BOTH = "both"
