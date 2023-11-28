from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleRentalTypeEnumeration(Enum):
    """
    Allowed values for VehiclePRentalModeOfOperation.
    """
    VEHICLE_HIRE = "vehicleHire"
    VEHICLE_LEASE = "vehicleLease"
