from dataclasses import dataclass

from .deck_entrance_assignment_ref_structure import DeckEntranceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignmentRef(DeckEntranceAssignmentRefStructure):
    class Meta:
        name = "deckEntranceAssignmentRef"
        namespace = "http://www.netex.org.uk/netex"
