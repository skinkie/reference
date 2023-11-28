from dataclasses import dataclass
from netex.infrastructure_point_version_structure import InfrastructurePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireJunctionVersionStructure(InfrastructurePointVersionStructure):
    """
    Type for WIRE JUNCTION.
    """
    class Meta:
        name = "WireJunction_VersionStructure"
