from dataclasses import dataclass
from netex.block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlockPartRefStructure(BlockPartRefStructure):
    """
    Type for a reference to a TRAIN BLOCK PART.
    """
