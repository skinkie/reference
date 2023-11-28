from dataclasses import dataclass, field
from netex.road_element_version_structure import RoadElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadElement(RoadElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a ROAD network.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
