from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TelecabinSubmodeEnumeration(Enum):
    """Values for Telecabin MODEs of TRANSPORT: TPEG pti_table_09, col_table_14."""
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    TELECABIN = "telecabin"
    CABLE_CAR = "cableCar"
    LIFT = "lift"
    CHAIR_LIFT = "chairLift"
    DRAG_LIFT = "dragLift"
    TELECABIN_LINK = "telecabinLink"
