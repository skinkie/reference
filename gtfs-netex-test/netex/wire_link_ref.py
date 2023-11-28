from dataclasses import dataclass
from netex.wire_link_ref_structure import WireLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireLinkRef(WireLinkRefStructure):
    """
    Reference to a WIRE LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
