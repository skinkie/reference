from dataclasses import dataclass
from netex.route_link_ref_by_value_structure import RouteLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteLinkRefByValue(RouteLinkRefByValueStructure):
    """
    Reference to a ROUTE LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
