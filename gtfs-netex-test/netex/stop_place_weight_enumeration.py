from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopPlaceWeightEnumeration(Enum):
    """Allowed values for INTERCHANGE classification at a STOP PLACE.

    +v1.1
    """
    INTERNATIONAL = "international"
    NATIONAL = "national"
    REGIONAL = "regional"
    LOCAL = "local"
