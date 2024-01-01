from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageLockerFacilityEnumeration(Enum):
    OTHER = "other"
    LOCKERS = "lockers"
    OVERSIZE_LOCKERS = "oversizeLockers"
    LEFT_LUGGAGE_COUNTER = "leftLuggageCounter"
    BIKE_RACK = "bikeRack"
    CLOAKROOM = "cloakroom"
