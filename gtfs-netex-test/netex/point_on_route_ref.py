from dataclasses import dataclass

from .point_on_route_ref_structure import PointOnRouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOnRouteRef(PointOnRouteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
