from dataclasses import dataclass
from netex.parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GaragePointRefStructure(ParkingPointRefStructure):
    """
    Type for a reference to a GARAGE POINT.
    """
