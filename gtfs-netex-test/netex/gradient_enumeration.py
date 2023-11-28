from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GradientEnumeration(Enum):
    """
    Allowed values for Gradient steepness.
    """
    VERY_STEEP = "verySteep"
    STEEP = "steep"
    MEDIUM = "medium"
    GENTLE = "gentle"
    LEVEL = "level"
