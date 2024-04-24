from dataclasses import dataclass

from .deck_level_version_structure import DeckLevelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckLevel(DeckLevelVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
