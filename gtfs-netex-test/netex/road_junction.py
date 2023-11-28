from dataclasses import dataclass, field
from netex.road_junction_version_structure import RoadJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadJunction(RoadJunctionVersionStructure):
    """
    A type of INFRASTRUCTURE POINT used to describe a ROAD network.

    :ivar id: Identifier of ROAD JUNCTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
