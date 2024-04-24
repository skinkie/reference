from dataclasses import dataclass

from .deck_entrance_version_structure import DeckEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntrance1(DeckEntranceVersionStructure):
    class Meta:
        name = "DeckEntrance"
        namespace = "http://www.netex.org.uk/netex"
