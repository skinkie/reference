from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_plan_assignment import DeckPlanAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckPlanAssignments_RelStructure"

    deck_plan_assignment: list[DeckPlanAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlanAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
