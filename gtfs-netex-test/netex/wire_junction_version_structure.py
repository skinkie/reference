from dataclasses import dataclass
from .infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireJunctionVersionStructure(InfrastructurePointVersionStructure):
    class Meta:
        name = "WireJunction_VersionStructure"
