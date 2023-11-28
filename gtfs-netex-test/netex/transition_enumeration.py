from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransitionEnumeration(Enum):
    """
    Allowed values for path transition.
    """
    UP = "up"
    DOWN = "down"
    LEVEL = "level"
    UP_AND_DOWN = "upAndDown"
    DOWN_AND_UP = "downAndUp"
