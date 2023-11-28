from dataclasses import dataclass, field
from netex.flexible_route_version_structure import FlexibleRouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleRoute(FlexibleRouteVersionStructure):
    """Specialisation of ROUTE for flexible service.

    May include both point and zonal areas and ordered and unordered
    sections.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
