from dataclasses import dataclass
from netex.railway_link_ref_structure import RailwayLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayLinkRef(RailwayLinkRefStructure):
    """
    Reference to a RAILWAY LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
