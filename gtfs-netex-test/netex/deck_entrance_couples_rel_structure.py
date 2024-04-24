from dataclasses import dataclass, field
from typing import List

from .deck_entrance_couple import DeckEntranceCouple
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceCouplesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckEntranceCouples_RelStructure"

    deck_entrance_couple: List[DeckEntranceCouple] = field(
        default_factory=list,
        metadata={
            "name": "DeckEntranceCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
