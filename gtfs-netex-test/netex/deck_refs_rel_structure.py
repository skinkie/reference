from dataclasses import dataclass, field
from typing import List

from .deck_ref import DeckRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckRefs_RelStructure"

    deck_ref: List[DeckRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
