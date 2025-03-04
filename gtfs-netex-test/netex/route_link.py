from dataclasses import dataclass

from .route_link_version_structure import RouteLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RouteLink(RouteLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
