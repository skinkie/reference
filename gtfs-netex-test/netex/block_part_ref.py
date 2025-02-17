from dataclasses import dataclass

from .block_part_ref_structure import BlockPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlockPartRef(BlockPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
