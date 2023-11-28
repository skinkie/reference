from dataclasses import dataclass
from netex.block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlockRef(BlockRefStructure):
    """
    Reference to a BLOCK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
