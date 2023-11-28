from dataclasses import dataclass
from netex.relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPointVersionStructure(ReliefPointVersionStructure):
    """
    Type for PARKING POINT.
    """
    class Meta:
        name = "ParkingPoint_VersionStructure"
