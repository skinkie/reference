from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DoorTypeEnumeration(Enum):
    HINGED_SINGLE = "hingedSingle"
    HINGED_PAIR = "hingedPair"
    SLIDING_SINGLE = "slidingSingle"
    SLIDING_PAIR = "slidingPair"
    FOLDING_SINGLE = "foldingSingle"
    FOLDING_PAIR = "foldingPair"
    HINGED_RAMP = "hingedRamp"
    REVOLVING = "revolving"
    OTHER = "other"
    NONE = "none"
    UNKNOWN = "unknown"
