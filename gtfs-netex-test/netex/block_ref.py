from dataclasses import dataclass

from .block_ref_structure import BlockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockRef(BlockRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
