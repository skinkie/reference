from dataclasses import dataclass

from .assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainComponentLabelAssignmentRefStructure(AssignmentRefStructure):
    pass
