from dataclasses import dataclass
from netex.road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadPointRef(RoadPointRefStructure):
    """
    Reference to a ROAD POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
