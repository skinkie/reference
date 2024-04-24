from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .level_in_structure import LevelInStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LevelsInStructureRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "levelsInStructure_RelStructure"

    level_in_structure: List[LevelInStructure] = field(
        default_factory=list,
        metadata={
            "name": "LevelInStructure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
