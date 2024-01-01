from dataclasses import dataclass
from .compound_block_ref_structure import CompoundBlockRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundBlockRef(CompoundBlockRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
