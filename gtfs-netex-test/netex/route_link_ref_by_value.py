from dataclasses import dataclass

from .route_link_ref_by_value_structure import RouteLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteLinkRefByValue(RouteLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
