from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NecessaryForceEnumeration(Enum):
    """
    Allowed values for the necessary force to open a door.
    """
    NO_FORCE = "noForce"
    LIGHT_FORCE = "lightForce"
    MEDIUM_FORCE = "mediumForce"
    HEAVY_FORCE = "heavyForce"
    UNKNOWN = "unknown"
