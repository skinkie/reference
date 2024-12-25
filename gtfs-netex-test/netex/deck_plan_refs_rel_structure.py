from dataclasses import dataclass, field

from .deck_plan_ref import DeckPlanRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckPlanRefs_RelStructure"

    deck_plan_ref: list[DeckPlanRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlanRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
