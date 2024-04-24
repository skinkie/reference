from dataclasses import dataclass

from .deck_entrance_version_structure import DeckEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckEntranceVersionStructure(DeckEntranceVersionStructure):
    class Meta:
        name = "OtherDeckEntrance_VersionStructure"
