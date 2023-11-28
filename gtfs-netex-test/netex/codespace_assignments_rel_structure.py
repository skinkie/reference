from dataclasses import dataclass, field
from typing import List
from netex.codespace_assignment_versioned_child_structure import CodespaceAssignmentVersionedChildStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceAssignmentsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CODESPACE  ASSIGNMENT.

    :ivar codespace_assignment: Assignment of use of a CODESPACE with
        responsibility for managing data within a given ZONE.
    """
    class Meta:
        name = "codespaceAssignments_RelStructure"

    codespace_assignment: List[CodespaceAssignmentVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "CodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
