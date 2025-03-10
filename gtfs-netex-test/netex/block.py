from dataclasses import dataclass

from .block_version_structure import BlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Block(BlockVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
