from dataclasses import dataclass
from netex.topographic_projection_ref_structure import TopographicProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicProjectionRef(TopographicProjectionRefStructure):
    """
    Reference to a TOPOGRAPHIC PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
