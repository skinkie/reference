from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ChildSeatEnumeration(Enum):
    """Allowed values for ChildSeat.

    +v1.2.2
    """
    BABY = "baby"
    SMALL_CHILD = "smallChild"
    OLDER_CHILD = "olderChild"
    NONE = "none"
    OTHER = "other"
