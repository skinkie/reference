from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockerTypeEnumeration(Enum):
    LEFT_LUGGAGE_OFFICE = "leftLuggageOffice"
    LOCKERS = "lockers"
    OVERSIZE_LOCKERS = "oversizeLockers"
    BIKE_RACK = "bikeRack"
    BIKE_CARRIAGE = "bikeCarriage"
    OTHER = "other"
