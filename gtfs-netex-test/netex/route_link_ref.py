from dataclasses import dataclass

from .route_link_ref_structure import RouteLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RouteLinkRef(RouteLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
