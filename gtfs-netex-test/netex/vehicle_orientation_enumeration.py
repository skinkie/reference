from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleOrientationEnumeration(Enum):
    """
    Allowed values for Vehicle Orientation.
    """
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    UNKNOWN = "unknown"
