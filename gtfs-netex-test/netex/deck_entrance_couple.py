from dataclasses import dataclass

from .deck_entrance_couple_versioned_child_structure import DeckEntranceCoupleVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceCouple(DeckEntranceCoupleVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
