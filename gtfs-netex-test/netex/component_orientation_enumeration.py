from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ComponentOrientationEnumeration(Enum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    UNKNOWN = "unknown"
    LEFTWARDS = "leftwards"
    RIGHTWARDS = "rightwards"
    ANGLED_LEFT = "angledLeft"
    ANGLED_RIGHT = "angledRight"
    ANGLED_BACK_LEFT = "angledBackLeft"
    ANGLED_BACK_RIGHT = "angledBackRight"
