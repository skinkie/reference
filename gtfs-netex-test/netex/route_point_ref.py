from dataclasses import dataclass
from .route_point_ref_structure import RoutePointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePointRef(RoutePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
