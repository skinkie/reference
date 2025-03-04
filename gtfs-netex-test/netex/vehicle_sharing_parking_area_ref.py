from dataclasses import dataclass

from .vehicle_sharing_parking_area_ref_structure import VehicleSharingParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleSharingParkingAreaRef(VehicleSharingParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
