from dataclasses import dataclass
from netex.parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPointRef(ParkingPointRefStructure):
    """
    Reference to a PARKING POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
