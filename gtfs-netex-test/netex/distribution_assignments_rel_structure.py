from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.distribution_assignment import DistributionAssignment
from netex.distribution_assignment_ref import DistributionAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DISTRIBUTION ASSIGNMENTs.
    """
    class Meta:
        name = "distributionAssignments_RelStructure"

    distribution_assignment_ref_or_distribution_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionAssignmentRef",
                    "type": DistributionAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionAssignment",
                    "type": DistributionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
