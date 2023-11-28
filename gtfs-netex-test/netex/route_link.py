from dataclasses import dataclass, field
from netex.route_link_version_structure import RouteLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteLink(RouteLinkVersionStructure):
    """An oriented link between two ROUTE POINTs allowing the definition of a
    unique path through the network.

    Because ROUTE LINKs are directional   there will be separate links
    for each direction of a route.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
