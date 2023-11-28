from dataclasses import dataclass
from netex.line_network_ref_structure import LineNetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineNetworkRef(LineNetworkRefStructure):
    """
    Reference to a LINE NETWORK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
