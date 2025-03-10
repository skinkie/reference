from dataclasses import dataclass

from .train_block_part_version_structure import TrainBlockPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainBlockPart(TrainBlockPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
