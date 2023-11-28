from dataclasses import dataclass
from netex.point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointVersionStructure(PointVersionStructure):
    """
    Type for VEHICLE MEETING POINT restricts id.
    """
    class Meta:
        name = "VehicleMeetingPoint_VersionStructure"
