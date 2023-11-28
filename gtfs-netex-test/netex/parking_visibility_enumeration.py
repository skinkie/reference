from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingVisibilityEnumeration(Enum):
    """
    Allowed values for PARKING Visibility.
    """
    UNMARKED = "unmarked"
    SIGNAGE_ONLY = "signageOnly"
    DEMARCATED = "demarcated"
    DOCKS = "docks"
    OTHER = "other"
