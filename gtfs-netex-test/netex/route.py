from dataclasses import dataclass

from .route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Route(RouteVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
