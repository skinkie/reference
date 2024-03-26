from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntrancePurposeEnumeration(Enum):
    MAIN = "main"
    SIDE = "side"
    BACK = "back"
    SECONDARY = "secondary"
    WITHIN_STOP_PLACE = "withinStopPlace"
    EMERGENCY_ONLY = "emergencyOnly"
    OTHER = "other"
