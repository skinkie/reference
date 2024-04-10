from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TelecabinSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    TELECABIN = "telecabin"
    CABLE_CAR = "cableCar"
    LIFT = "lift"
    CHAIR_LIFT = "chairLift"
    DRAG_LIFT = "dragLift"
    PATERNOSTER = "paternoster"
    TELECABIN_LINK = "telecabinLink"
