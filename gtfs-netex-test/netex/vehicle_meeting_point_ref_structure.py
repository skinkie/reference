from dataclasses import dataclass
from netex.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointRefStructure(PointRefStructure):
    """
    Type for a reference to a VEHICLE MEETING POINT.
    """
