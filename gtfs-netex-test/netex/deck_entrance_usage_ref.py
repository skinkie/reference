from dataclasses import dataclass

from .deck_entrance_usage_ref_structure import DeckEntranceUsageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceUsageRef(DeckEntranceUsageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
