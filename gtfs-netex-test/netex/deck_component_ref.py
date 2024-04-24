from dataclasses import dataclass

from .deck_component_ref_structure import DeckComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckComponentRef(DeckComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
