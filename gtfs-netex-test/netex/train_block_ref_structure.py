from dataclasses import dataclass
from netex.block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlockRefStructure(BlockRefStructure):
    """
    Type for a reference to a TRAIN BLOCK.
    """
