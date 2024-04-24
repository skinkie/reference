from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_level import DeckLevel

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckLevelsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckLevels_RelStructure"

    deck_level: List[DeckLevel] = field(
        default_factory=list,
        metadata={
            "name": "DeckLevel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
