from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TelecabinSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    TELECABIN = "telecabin"
    CABLE_CAR = "cableCar"
    LIFT = "lift"
    CHAIR_LIFT = "chairLift"
    DRAG_LIFT = "dragLift"
    TELECABIN_LINK = "telecabinLink"
