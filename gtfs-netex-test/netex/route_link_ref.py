from dataclasses import dataclass
from .route_link_ref_structure import RouteLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteLinkRef(RouteLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
