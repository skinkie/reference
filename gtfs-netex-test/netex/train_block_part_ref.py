from dataclasses import dataclass
from netex.train_block_part_ref_structure import TrainBlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlockPartRef(TrainBlockPartRefStructure):
    """
    Reference to a TRAIN BLOCK PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
