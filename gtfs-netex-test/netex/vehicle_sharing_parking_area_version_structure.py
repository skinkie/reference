from dataclasses import dataclass
from netex.parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingAreaVersionStructure(ParkingAreaVersionStructure):
    """
    Type for VEHICLE SHARING PARKING AREA.
    """
    class Meta:
        name = "VehicleSharingParkingArea_VersionStructure"
