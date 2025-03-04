from dataclasses import dataclass

from .parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleSharingParkingAreaVersionStructure(ParkingAreaVersionStructure):
    class Meta:
        name = "VehicleSharingParkingArea_VersionStructure"
