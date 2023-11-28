from dataclasses import dataclass
from netex.railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayPointRef(RailwayPointRefStructure):
    """
    Reference to a RAILWAY POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
