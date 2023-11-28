from dataclasses import dataclass
from netex.relief_point_ref_structure import ReliefPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPointRefStructure(ReliefPointRefStructure):
    """
    Type for a reference to a PARKING POINT.
    """
