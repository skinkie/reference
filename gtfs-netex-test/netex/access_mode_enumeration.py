from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessModeEnumeration(Enum):
    FOOT = "foot"
    BICYCLE = "bicycle"
    BOAT = "boat"
    CAR = "car"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
    SKI = "ski"
    SKATE = "skate"
    MOTORCYCLE = "motorcycle"
    SCOOTER = "scooter"
