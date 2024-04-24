from dataclasses import dataclass

from .deck_window_version_structure import DeckWindowVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckWindow(DeckWindowVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
