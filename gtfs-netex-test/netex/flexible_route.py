from dataclasses import dataclass
from .flexible_route_version_structure import FlexibleRouteVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleRoute(FlexibleRouteVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
