from dataclasses import dataclass, field
from netex.block_version_structure import BlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Block(BlockVersionStructure):
    """The work of a vehicle from the time it leaves a PARKING POINT after parking
    until its next return to park at a PARKING POINT.

    Any subsequent departure from a PARKING POINT after parking marks
    the start of a new BLOCK. The period of a BLOCK has to be covered by
    DUTies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
