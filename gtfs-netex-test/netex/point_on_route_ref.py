from dataclasses import dataclass
from netex.point_on_route_ref_structure import PointOnRouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnRouteRef(PointOnRouteRefStructure):
    """
    Reference to POINT ON ROUTE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
