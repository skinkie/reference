from dataclasses import dataclass, field
from netex.direction_value_structure import DirectionValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Direction(DirectionValueStructure):
    """
    A classification for the general orientation of ROUTEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
