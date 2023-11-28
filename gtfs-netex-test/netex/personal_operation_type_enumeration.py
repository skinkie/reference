from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PersonalOperationTypeEnumeration(Enum):
    """
    Allowed values for VehiclePoolingModeOfOperation.
    """
    OWN_CAR = "ownCar"
    PRIVATE_LIFT = "privateLift"
