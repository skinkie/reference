from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DrivingStyleEnumeration(Enum):
    SEDATE = "sedate"
    MODERATE = "moderate"
    FAST = "fast"
    OTHER = "other"
