from dataclasses import dataclass
from netex.point_projection_ref_structure import PointProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointProjectionRef(PointProjectionRefStructure):
    """
    Reference to a PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
