from dataclasses import dataclass
from netex.block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlockPartRef(BlockPartRefStructure):
    """
    Reference to a BLOCK PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
