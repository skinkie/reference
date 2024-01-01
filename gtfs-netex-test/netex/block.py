from dataclasses import dataclass
from .block_version_structure import BlockVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Block(BlockVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
