from dataclasses import dataclass, field
from netex.railway_element_version_structure import RailwayElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayElement(RailwayElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a RAILWAY network.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
