from dataclasses import dataclass
from netex.link_projection_ref_structure import LinkProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkProjectionRef(LinkProjectionRefStructure):
    """
    Reference to a PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
