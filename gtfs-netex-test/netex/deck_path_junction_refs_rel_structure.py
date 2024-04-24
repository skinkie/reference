from dataclasses import dataclass, field
from typing import List

from .deck_path_junction import DeckPathJunction
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathJunctionRefsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckPathJunctionRefs_RelStructure"

    deck_path_junction: List[DeckPathJunction] = field(
        default_factory=list,
        metadata={
            "name": "DeckPathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
