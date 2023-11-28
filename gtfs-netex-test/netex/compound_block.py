from dataclasses import dataclass, field
from netex.compound_block_structure import CompoundBlockStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompoundBlock(CompoundBlockStructure):
    """A composite BLOCK formed of several BLOCKs coupled together during a certain
    period.

    Any coupling or separation action marks the start of a new COMPOUND
    BLOCK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
