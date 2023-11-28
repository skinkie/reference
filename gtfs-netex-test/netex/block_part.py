from dataclasses import dataclass, field
from netex.block_part_version_structure import BlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlockPart(BlockPartVersionStructure):
    """
    A part of a BLOCK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
