from dataclasses import dataclass
from netex.train_block_ref_structure import TrainBlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlockRef(TrainBlockRefStructure):
    """
    Reference to a TRAIN BLOCK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
