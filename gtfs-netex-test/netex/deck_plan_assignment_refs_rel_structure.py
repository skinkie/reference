from dataclasses import dataclass, field

from .deck_plan_assignment_ref import DeckPlanAssignmentRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckPlanAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckPlanAssignmentRefs_RelStructure"

    deck_plan_assignment_ref: list[DeckPlanAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlanAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
