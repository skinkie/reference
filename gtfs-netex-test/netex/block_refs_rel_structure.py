from dataclasses import dataclass, field
from typing import Union

from .block_ref import BlockRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .train_block_ref import TrainBlockRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlockRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "blockRefs_RelStructure"

    block_ref: list[Union[TrainBlockRef, BlockRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
