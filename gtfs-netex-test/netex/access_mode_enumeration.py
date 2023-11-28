from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessModeEnumeration(Enum):
    """
    Allowed values for Access MODEs for SITEs.
    """
    FOOT = "foot"
    BICYCLE = "bicycle"
    BOAT = "boat"
    CAR = "car"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
    SKI = "ski"
    SKATE = "skate"
    MOTORCYCLE = "motorcycle"
    SCOOTER = "scooter"
