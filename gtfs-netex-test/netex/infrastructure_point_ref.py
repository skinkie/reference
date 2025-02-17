from dataclasses import dataclass

from .infrastructure_point_ref_structure import InfrastructurePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfrastructurePointRef(InfrastructurePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
