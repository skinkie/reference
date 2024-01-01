from dataclasses import dataclass
from .block_part_version_structure import BlockPartVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlockPart(BlockPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
