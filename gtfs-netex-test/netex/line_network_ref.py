from dataclasses import dataclass

from .line_network_ref_structure import LineNetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LineNetworkRef(LineNetworkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
