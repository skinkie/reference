from dataclasses import dataclass

from .deck_space_ref_structure import DeckSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerSpaceRefStructure(DeckSpaceRefStructure):
    pass
