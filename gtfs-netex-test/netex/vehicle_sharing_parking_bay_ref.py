from dataclasses import dataclass
from .vehicle_sharing_parking_bay_ref_structure import (
    VehicleSharingParkingBayRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingParkingBayRef(VehicleSharingParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
