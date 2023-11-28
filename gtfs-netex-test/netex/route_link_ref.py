from dataclasses import dataclass
from netex.route_link_ref_structure import RouteLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteLinkRef(RouteLinkRefStructure):
    """
    Reference to a ROUTE LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
