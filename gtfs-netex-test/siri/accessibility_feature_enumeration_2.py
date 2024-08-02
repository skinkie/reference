from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AccessibilityFeatureEnumeration2(Enum):
    UNKNOWN = "unknown"
    SINGLE_STEP = "singleStep"
    STAIRS = "stairs"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    LIFT = "lift"
    RAMP = "ramp"
    MIND_THE_GAP = "mindTheGap"
    TACTILE_PAVING = "tactilePaving"
    SERIES_OF_STAIRS = "seriesOfStairs"
    SHUTTLE = "shuttle"
    BARRIER = "barrier"
    NARROW_ENTRANCE = "narrowEntrance"
    CONFINED_SPACE = "confinedSpace"
    QUEUE_MANAGEMENT = "queueManagement"
    NONE = "none"
    OTHER = "other"
    UNDEFINED = "undefined"
