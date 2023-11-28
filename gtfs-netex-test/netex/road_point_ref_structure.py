from dataclasses import dataclass
from netex.infrastructure_point_ref_structure import InfrastructurePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadPointRefStructure(InfrastructurePointRefStructure):
    """
    Type for Reference to a ROAD POINT.
    """
