from dataclasses import dataclass

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfrastructurePointVersionStructure(PointVersionStructure):
    class Meta:
        name = "InfrastructurePoint_VersionStructure"
