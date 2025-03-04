from dataclasses import dataclass

from .flexible_route_version_structure import FlexibleRouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleRoute(FlexibleRouteVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
