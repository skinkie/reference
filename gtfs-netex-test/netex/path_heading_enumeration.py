from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PathHeadingEnumeration(Enum):
    """
    Allowed values for path heading.
    """
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACK = "back"
