from dataclasses import dataclass

from .deck_place_in_sequence_ref_structure import DeckPlaceInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlaceInSequenceRef(DeckPlaceInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
