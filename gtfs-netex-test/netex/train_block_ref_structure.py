from dataclasses import dataclass

from .block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainBlockRefStructure(BlockRefStructure):
    pass
