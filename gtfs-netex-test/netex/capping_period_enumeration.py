from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CappingPeriodEnumeration(Enum):
    """
    Allowed values for CAPPING PERIOD.
    """
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    NONE = "none"
