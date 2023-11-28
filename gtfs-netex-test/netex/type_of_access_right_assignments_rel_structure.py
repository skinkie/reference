from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfAccessRightAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF ACCESS RIGHT ASSIGNMENTs.
    """
    class Meta:
        name = "TypeOfAccessRightAssignments_RelStructure"

    type_of_access_right_assignment_ref_or_type_of_access_right_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfAccessRightAssignmentRef",
                    "type": TypeOfAccessRightAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
