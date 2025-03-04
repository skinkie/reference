from dataclasses import dataclass

from .parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingParkingAreaVersionStructure(ParkingAreaVersionStructure):
    class Meta:
        name = "VehiclePoolingParkingArea_VersionStructure"
