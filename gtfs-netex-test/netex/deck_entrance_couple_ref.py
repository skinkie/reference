from dataclasses import dataclass

from .deck_entrance_couple_ref_structure import DeckEntranceCoupleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceCoupleRef(DeckEntranceCoupleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
