from dataclasses import dataclass

from .deck_version_structure import DeckVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Deck(DeckVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
