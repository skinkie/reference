from dataclasses import dataclass
from netex.wire_link_ref_by_value_structure import WireLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireLinkRefByValue(WireLinkRefByValueStructure):
    """
    Reference to a WIRE LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
