from dataclasses import dataclass, field

from .deck_space_capacity import DeckSpaceCapacity
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckSpaceCapacitiesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckSpaceCapacities_RelStructure"

    deck_space_capacity: list[DeckSpaceCapacity] = field(
        default_factory=list,
        metadata={
            "name": "DeckSpaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
