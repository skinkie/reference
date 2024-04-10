from dataclasses import dataclass

from .routing_version_structure import RoutingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Routing(RoutingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
