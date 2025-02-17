from dataclasses import dataclass

from .deck_ref_structure import DeckRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckRef(DeckRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
