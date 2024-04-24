from dataclasses import dataclass

from .deck_entrance_usage_versioned_child_structure import DeckEntranceUsageVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceUsage(DeckEntranceUsageVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
