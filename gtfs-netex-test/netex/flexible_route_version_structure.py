from dataclasses import dataclass, field
from typing import Optional

from .flexible_route_type_enumeration import FlexibleRouteTypeEnumeration
from .route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleRouteVersionStructure(RouteVersionStructure):
    class Meta:
        name = "FlexibleRoute_VersionStructure"

    flexible_route_type: Optional[FlexibleRouteTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleRouteType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
