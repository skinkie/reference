from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrameNatureEnumeration(Enum):
    """
    Allowed values for Nature of data  in frame.
    """
    PLANNED = "planned"
    OPERATIONAL = "operational"
    CONTINGENCY_PLAN = "contingencyPlan"
    OTHER = "other"
