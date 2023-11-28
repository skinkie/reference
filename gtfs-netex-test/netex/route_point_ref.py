from dataclasses import dataclass
from netex.route_point_ref_structure import RoutePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutePointRef(RoutePointRefStructure):
    """
    Reference to a ROUTE POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
