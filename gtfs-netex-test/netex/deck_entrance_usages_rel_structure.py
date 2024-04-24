from dataclasses import dataclass, field
from typing import List

from .deck_entrance_usage import DeckEntranceUsage
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceUsagesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckEntranceUsages_RelStructure"

    deck_entrance_usage: List[DeckEntranceUsage] = field(
        default_factory=list,
        metadata={
            "name": "DeckEntranceUsage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
