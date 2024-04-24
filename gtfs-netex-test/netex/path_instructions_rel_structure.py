from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_instruction import PathInstruction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathInstructionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pathInstructions_RelStructure"

    path_instruction: List[PathInstruction] = field(
        default_factory=list,
        metadata={
            "name": "PathInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
