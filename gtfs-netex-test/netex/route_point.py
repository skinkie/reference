from dataclasses import dataclass, field
from netex.route_point_version_structure import RoutePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutePoint(RoutePointVersionStructure):
    """
    A POINT used to define the shape of a ROUTE through the network.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
