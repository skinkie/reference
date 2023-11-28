from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CongestionEnumeration(Enum):
    """
    Allowed values for a congestion.
    """
    NO_WAITING = "noWaiting"
    QUEUE = "queue"
    CROWDING = "crowding"
    FULL = "full"
