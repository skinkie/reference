from dataclasses import dataclass

from .deck_entrance_assignment_version_structure import DeckEntranceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignment(DeckEntranceAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
