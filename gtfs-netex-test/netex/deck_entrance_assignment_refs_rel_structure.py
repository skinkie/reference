from dataclasses import dataclass, field
from typing import List

from .deck_entrance_assignment_ref import DeckEntranceAssignmentRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckEntranceAssignmentRefs_RelStructure"

    deck_entrance_assignment_ref: List[DeckEntranceAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "deckEntranceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
