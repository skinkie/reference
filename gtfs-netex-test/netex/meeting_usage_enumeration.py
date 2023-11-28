from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingUsageEnumeration(Enum):
    """Allowed values for Meeting Usage.

    +v1.2.2
    """
    PICK_UP = "pickUp"
    SET_DOWN = "setDown"
    ALL = "all"
