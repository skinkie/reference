from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameStationReentryPolicyEnumeration(Enum):
    BLOCKED = "blocked"
    NEW_FARE = "newFare"
    MAXIMUM_FARE = "maximumFare"
    ALLOWED = "allowed"
