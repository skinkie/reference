from dataclasses import dataclass
from netex.parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingAreaVersionStructure(ParkingAreaVersionStructure):
    """
    Type for VEHICLE POOLING PARKING AREA.
    """
    class Meta:
        name = "VehiclePoolingParkingArea_VersionStructure"
