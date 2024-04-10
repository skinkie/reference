from dataclasses import dataclass

from .infrastructure_point_version_structure import InfrastructurePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructurePoint(InfrastructurePointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
