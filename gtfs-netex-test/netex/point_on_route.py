from dataclasses import dataclass

from .point_on_route_versioned_child_structure import PointOnRouteVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOnRoute(PointOnRouteVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
