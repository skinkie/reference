from dataclasses import dataclass
from netex.route_derived_view_structure import RouteDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteView(RouteDerivedViewStructure):
    """
    Annotated reference to a ROUTE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
