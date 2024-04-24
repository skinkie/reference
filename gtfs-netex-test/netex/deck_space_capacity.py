from dataclasses import dataclass

from .deck_space_capacity_versioned_child_structure import DeckSpaceCapacityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpaceCapacity(DeckSpaceCapacityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
