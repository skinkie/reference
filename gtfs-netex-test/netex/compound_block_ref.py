from dataclasses import dataclass

from .compound_block_ref_structure import CompoundBlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CompoundBlockRef(CompoundBlockRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
