from dataclasses import dataclass
from netex.route_ref_structure import RouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteRef(RouteRefStructure):
    """
    Reference to a ROUTE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
