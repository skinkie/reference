from dataclasses import dataclass
from netex.parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GaragePointVersionStructure(ParkingPointVersionStructure):
    """
    Type for GARAGE POINT.
    """
    class Meta:
        name = "GaragePoint_VersionStructure"
