from dataclasses import dataclass, field
from netex.train_block_version_structure import TrainBlockVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainBlock(TrainBlockVersionStructure):
    """A composite train formed of several BLOCKs coupled together during a certain
    period.

    Any coupling or separation action marks the start of a new TRAIN
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
