from dataclasses import dataclass
from netex.point_in_sequence_ref_structure import PointInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnRouteRefStructure(PointInSequenceRefStructure):
    """
    Type for a reference to a POINT ON ROUTE.
    """
