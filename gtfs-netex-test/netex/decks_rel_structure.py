from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck import Deck

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DecksRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "decks_RelStructure"

    deck: list[Deck] = field(
        default_factory=list,
        metadata={
            "name": "Deck",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
