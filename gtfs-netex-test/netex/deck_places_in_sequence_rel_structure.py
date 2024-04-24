from dataclasses import dataclass, field
from typing import List

from .deck_place_in_sequence import DeckPlaceInSequence
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlacesInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckPlacesInSequence_RelStructure"

    deck_place_in_sequence: List[DeckPlaceInSequence] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlaceInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
