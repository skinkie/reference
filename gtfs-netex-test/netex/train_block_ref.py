from dataclasses import dataclass

from .train_block_ref_structure import TrainBlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockRef(TrainBlockRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
