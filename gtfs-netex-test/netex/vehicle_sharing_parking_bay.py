from dataclasses import dataclass

from .vehicle_sharing_parking_bay_version_structure import VehicleSharingParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleSharingParkingBay(VehicleSharingParkingBayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
