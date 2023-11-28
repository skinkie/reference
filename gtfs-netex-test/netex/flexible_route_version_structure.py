from dataclasses import dataclass, field
from typing import Optional
from netex.flexible_route_type_enumeration import FlexibleRouteTypeEnumeration
from netex.route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleRouteVersionStructure(RouteVersionStructure):
    """
    Type for a FLEXIBLE ROUTE.

    :ivar flexible_route_type: Type of FLEXIBLE ROUTE.
    """
    class Meta:
        name = "FlexibleRoute_VersionStructure"

    flexible_route_type: Optional[FlexibleRouteTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleRouteType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
