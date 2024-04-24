from dataclasses import dataclass, field
from typing import List

from .deck_navigation_path_ref import DeckNavigationPathRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckNavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckNavigationPathRefs_RelStructure"

    deck_navigation_path_ref: List[DeckNavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckNavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
