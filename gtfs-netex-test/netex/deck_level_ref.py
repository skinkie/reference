from dataclasses import dataclass

from .deck_level_ref_structure import DeckLevelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckLevelRef(DeckLevelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
