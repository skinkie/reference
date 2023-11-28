from dataclasses import dataclass
from netex.train_size_structure import TrainSizeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainSize(TrainSizeStructure):
    """
    Requirements for TRAIN SIZe.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
