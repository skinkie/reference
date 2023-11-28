from dataclasses import dataclass
from netex.parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingParkingBayVersionStructure(ParkingBayVersionStructure):
    """
    Type for VEHICLE SHARING PARKING BAY.
    """
    class Meta:
        name = "VehicleSharingParkingBay_VersionStructure"
