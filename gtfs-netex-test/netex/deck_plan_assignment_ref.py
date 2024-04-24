from dataclasses import dataclass

from .deck_plan_assignment_ref_structure import DeckPlanAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanAssignmentRef(DeckPlanAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
