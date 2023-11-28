from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageLockerFacilityEnumeration(Enum):
    """
    Allowed values for Luggage Locker Facility.

    :cvar OTHER:
    :cvar LOCKERS: pti23_17
    :cvar OVERSIZE_LOCKERS:
    :cvar LEFT_LUGGAGE_COUNTER:
    :cvar BIKE_RACK:
    :cvar CLOAKROOM:
    """
    OTHER = "other"
    LOCKERS = "lockers"
    OVERSIZE_LOCKERS = "oversizeLockers"
    LEFT_LUGGAGE_COUNTER = "leftLuggageCounter"
    BIKE_RACK = "bikeRack"
    CLOAKROOM = "cloakroom"
