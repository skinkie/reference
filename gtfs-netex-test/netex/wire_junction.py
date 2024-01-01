from dataclasses import dataclass
from .wire_junction_version_structure import WireJunctionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireJunction(WireJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
