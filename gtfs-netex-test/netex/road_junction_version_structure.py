from dataclasses import dataclass

from .infrastructure_point_version_structure import InfrastructurePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoadJunctionVersionStructure(InfrastructurePointVersionStructure):
    class Meta:
        name = "RoadJunction_VersionStructure"
