from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GradientEnumeration(Enum):
    VERY_STEEP = "verySteep"
    STEEP = "steep"
    MEDIUM = "medium"
    GENTLE = "gentle"
    LEVEL = "level"
