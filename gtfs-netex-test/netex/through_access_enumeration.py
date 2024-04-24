from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ThroughAccessEnumeration(Enum):
    NO_THROUGH_ACCESS = "noThroughAccess"
    OPEN_ENTRANCE = "openEntrance"
    DOOR = "door"
    UNKNOWN = "unknown"
