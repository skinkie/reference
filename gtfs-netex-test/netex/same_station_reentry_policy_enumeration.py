from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameStationReentryPolicyEnumeration(Enum):
    """
    Allowed values for Same Station Rentry Policy.
    """
    BLOCKED = "blocked"
    NEW_FARE = "newFare"
    MAXIMUM_FARE = "maximumFare"
    ALLOWED = "allowed"
