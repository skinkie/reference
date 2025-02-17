from dataclasses import dataclass

from .deck_entrance_ref_structure import DeckEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerEntranceRefStructure(DeckEntranceRefStructure):
    pass
