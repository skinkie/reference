from dataclasses import dataclass
from .train_block_part_version_structure import TrainBlockPartVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockPart(TrainBlockPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
