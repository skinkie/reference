from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelationToVehicleEnumeration(Enum):
    """
    Allowed values for Relation to vehicle.
    """
    FRONT_LEFT = "frontLeft"
    FRONT_RIGHT = "frontRight"
    BACK_RIGHT = "backRight"
    DRIVER_LEFT = "driverLeft"
    DRIVER_RIGHT = "driverRight"
