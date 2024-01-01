from dataclasses import dataclass
from .route_ref_structure import RouteRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteRef(RouteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
