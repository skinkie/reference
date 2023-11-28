from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlexibleServiceEnumeration(Enum):
    """Allowed values for flexible service type: FixedPassingTimes, DynamicPassingTimes, FixedHeadwayFrequency."""
    DYNAMIC_PASSING_TIMES = "dynamicPassingTimes"
    FIXED_HEADWAY_FREQUENCY = "fixedHeadwayFrequency"
    FIXED_PASSING_TIMES = "fixedPassingTimes"
    NOT_FLEXIBLE = "notFlexible"
    OTHER = "other"
