from dataclasses import dataclass
from netex.projection_ref_structure import ProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointProjectionRefStructure(ProjectionRefStructure):
    """
    Type for a reference to a POINT PROJECTION.
    """
