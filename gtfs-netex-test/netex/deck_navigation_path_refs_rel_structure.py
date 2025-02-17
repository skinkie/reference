from dataclasses import dataclass, field

from .deck_navigation_path_ref import DeckNavigationPathRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckNavigationPathRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "deckNavigationPathRefs_RelStructure"

    deck_navigation_path_ref: list[DeckNavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckNavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
