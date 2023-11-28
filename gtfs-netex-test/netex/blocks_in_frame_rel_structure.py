from dataclasses import dataclass, field
from typing import List
from netex.block import Block
from netex.compound_block import CompoundBlock
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.train_block import TrainBlock

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlocksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of BLOCKS.
    """
    class Meta:
        name = "blocksInFrame_RelStructure"

    block_or_compound_block_or_train_block: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Block",
                    "type": Block,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlock",
                    "type": CompoundBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlock",
                    "type": TrainBlock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
