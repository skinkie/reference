from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleSideEnumeration(Enum):
    LEFT_SIDE = "leftSide"
    RIGHT_SIDE = "rightSide"
    FRONT_END = "frontEnd"
    BACK_END = "backEnd"
    INTERNAL = "internal"
    ABOVE = "above"
    BELOW = "below"
