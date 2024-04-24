from dataclasses import dataclass

from .deck_plan_assignment_version_structure import DeckPlanAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanAssignment(DeckPlanAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
