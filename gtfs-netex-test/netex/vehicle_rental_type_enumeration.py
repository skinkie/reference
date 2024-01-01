from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleRentalTypeEnumeration(Enum):
    VEHICLE_HIRE = "vehicleHire"
    VEHICLE_LEASE = "vehicleLease"
