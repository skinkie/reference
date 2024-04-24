from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_entrance_assignment import DeckEntranceAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckEntranceAssignments_RelStructure"

    deck_entrance_assignment: List[DeckEntranceAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DeckEntranceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
