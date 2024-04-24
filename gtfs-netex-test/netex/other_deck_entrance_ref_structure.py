from dataclasses import dataclass

from .deck_entrance_ref_structure import DeckEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckEntranceRefStructure(DeckEntranceRefStructure):
    pass
