from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.train_stop_assignment import TrainStopAssignment
from netex.train_stop_assignment_ref import TrainStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainStopAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a TRAIN STOP POINT ASSIGNMENT.
    """
    class Meta:
        name = "trainStopAssignments_RelStructure"

    train_stop_assignment_ref_or_train_stop_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainStopAssignmentRef",
                    "type": TrainStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
