from dataclasses import dataclass, field
from netex.railway_junction_version_structure import RailwayJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayJunction(RailwayJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a RAILWAY network.

    :ivar id: Identifier of RAILWAY JUNCTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
