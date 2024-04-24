from dataclasses import dataclass

from .deck_place_in_sequence_versioned_child_structure import DeckPlaceInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlaceInSequence(DeckPlaceInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
