from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundingMethodEnumeration(Enum):
    NONE = "none"
    DOWN = "down"
    UP = "up"
    SPLIT = "split"
    STEP_TABLE = "stepTable"
