from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PathHeadingEnumeration(Enum):
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACK = "back"
