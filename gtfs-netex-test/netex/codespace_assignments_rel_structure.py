from dataclasses import dataclass, field

from .codespace_assignment_versioned_child_structure import CodespaceAssignmentVersionedChildStructure
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CodespaceAssignmentsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "codespaceAssignments_RelStructure"

    codespace_assignment: list[CodespaceAssignmentVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "CodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
