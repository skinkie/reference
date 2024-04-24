from dataclasses import dataclass

from .deck_space_capacity_ref_structure import DeckSpaceCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpaceCapacityRef(DeckSpaceCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
