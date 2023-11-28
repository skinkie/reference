from dataclasses import dataclass
from netex.parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingBayVersionStructure(ParkingBayVersionStructure):
    """
    Type for VEHICLE POOLING PARKING BAY.
    """
    class Meta:
        name = "VehiclePoolingParkingBay_VersionStructure"
