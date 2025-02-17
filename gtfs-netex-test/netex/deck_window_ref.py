from dataclasses import dataclass

from .deck_window_ref_structure import DeckWindowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckWindowRef(DeckWindowRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
