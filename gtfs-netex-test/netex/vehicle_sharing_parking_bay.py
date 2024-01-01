from dataclasses import dataclass
from .vehicle_sharing_parking_bay_version_structure import (
    VehicleSharingParkingBayVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingParkingBay(VehicleSharingParkingBayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
