from dataclasses import dataclass, field
from netex.path_junction_version_structure import PathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathJunction(PathJunctionVersionStructure):
    """
    A designated point, inside or outside of a STOP PLACE or POINT OF INTEREST, at
    which two or more PATH LINKs may connect or branch.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
