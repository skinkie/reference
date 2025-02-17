from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_plan import DeckPlan

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckPlansRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckPlans_RelStructure"

    deck_plan: list[DeckPlan] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlan",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
