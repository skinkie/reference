from dataclasses import dataclass

from .deck_component_version_structure import DeckComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeckComponent(DeckComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
