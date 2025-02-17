from dataclasses import dataclass

from .train_block_version_structure import TrainBlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainBlock(TrainBlockVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
