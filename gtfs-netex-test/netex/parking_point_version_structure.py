from dataclasses import dataclass

from .relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingPointVersionStructure(ReliefPointVersionStructure):
    class Meta:
        name = "ParkingPoint_VersionStructure"
