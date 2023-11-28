from dataclasses import dataclass, field
from netex.routing_version_structure import RoutingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Routing(RoutingVersionStructure):
    """
    Limitations on routing of a fare.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
