from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class QueueManagementEnumeration(Enum):
    """
    Allowed value for Queue Management.
    """
    NONE = "none"
    MAZE = "maze"
    SEPARATE_LINES = "separateLines"
    TICKETED = "ticketed"
    OTHER = "other"
