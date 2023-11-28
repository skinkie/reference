from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassengerCommsFacilityEnumeration(Enum):
    """
    Allowed values for PASSENGER COMMUNICATIONS FACILITY.

    :cvar UNKNOWN:
    :cvar FREE_WIFI:
    :cvar PUBLIC_WIFI:
    :cvar POWER_SUPPLY_SOCKETS:
    :cvar TELEPHONE: pti23_21
    :cvar AUDIO_ENTERTAINMENT: pti23_14
    :cvar VIDEO_ENTERTAINMENT: pti23_15
    :cvar BUSINESS_SERVICES: pti23_25
    :cvar INTERNET:
    :cvar POST_OFFICE:
    :cvar POST_BOX:
    """
    UNKNOWN = "unknown"
    FREE_WIFI = "freeWifi"
    PUBLIC_WIFI = "publicWifi"
    POWER_SUPPLY_SOCKETS = "powerSupplySockets"
    TELEPHONE = "telephone"
    AUDIO_ENTERTAINMENT = "audioEntertainment"
    VIDEO_ENTERTAINMENT = "videoEntertainment"
    BUSINESS_SERVICES = "businessServices"
    INTERNET = "internet"
    POST_OFFICE = "postOffice"
    POST_BOX = "postBox"
