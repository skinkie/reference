from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class CongestionEnumeration(Enum):
    NO_WAITING = "noWaiting"
    QUEUE = "queue"
    CROWDING = "crowding"
    FULL = "full"
