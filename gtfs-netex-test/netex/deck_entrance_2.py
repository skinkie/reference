from dataclasses import dataclass

from .deck_component_version_structure import DeckComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntrance2(DeckComponentVersionStructure):
    class Meta:
        name = "DeckEntrance_"
        namespace = "http://www.netex.org.uk/netex"
