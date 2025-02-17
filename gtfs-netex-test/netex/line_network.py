from dataclasses import dataclass

from .line_network_version_structure import LineNetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LineNetwork(LineNetworkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
