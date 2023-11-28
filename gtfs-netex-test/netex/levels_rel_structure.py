from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.level import Level
from netex.level_ref import LevelRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LevelsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LEVELs.
    """
    class Meta:
        name = "levels_RelStructure"

    level_ref_or_level: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LevelRef",
                    "type": LevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Level",
                    "type": Level,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
