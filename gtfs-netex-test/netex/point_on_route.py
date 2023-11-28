from dataclasses import dataclass, field
from netex.point_on_route_versioned_child_structure import PointOnRouteVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnRoute(PointOnRouteVersionedChildStructure):
    """
    A reference to a ROUTE POINT used to define a ROUTE with its order on that
    ROUTE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
