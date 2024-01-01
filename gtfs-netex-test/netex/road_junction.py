from dataclasses import dataclass
from .road_junction_version_structure import RoadJunctionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadJunction(RoadJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
