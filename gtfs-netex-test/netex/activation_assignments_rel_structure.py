from dataclasses import dataclass, field
from typing import List
from netex.activation_assignment import ActivationAssignment
from netex.activation_assignment_ref import ActivationAssignmentRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ACTIVATION ASSIGNMENTs.
    """
    class Meta:
        name = "activationAssignments_RelStructure"

    activation_assignment_ref_or_activation_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActivationAssignmentRef",
                    "type": ActivationAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationAssignment",
                    "type": ActivationAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
