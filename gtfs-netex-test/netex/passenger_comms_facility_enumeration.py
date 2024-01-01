from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassengerCommsFacilityEnumeration(Enum):
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
