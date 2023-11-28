from dataclasses import dataclass
from netex.routing_ref_structure import RoutingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutingRef(RoutingRefStructure):
    """
    Reference to a ROUTING PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
