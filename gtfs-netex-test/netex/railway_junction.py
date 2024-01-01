from dataclasses import dataclass
from .railway_junction_version_structure import RailwayJunctionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayJunction(RailwayJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
