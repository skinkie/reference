from dataclasses import dataclass, field
from netex.line_network_version_structure import LineNetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineNetwork(LineNetworkVersionStructure):
    """A description of the topological connectivity of a LINE as a set of LINE
    SECTIONs.

    This is sufficient to draw a route map for the whole line including
    branches and loops.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
