from dataclasses import dataclass
from .routing_ref_structure import RoutingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingRef(RoutingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
