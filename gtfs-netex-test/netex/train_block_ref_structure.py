from dataclasses import dataclass
from .block_ref_structure import BlockRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainBlockRefStructure(BlockRefStructure):
    value: RestrictedVar
