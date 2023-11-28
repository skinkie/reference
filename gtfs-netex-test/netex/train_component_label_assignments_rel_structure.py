from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.train_component_label_assignment import TrainComponentLabelAssignment
from netex.train_component_label_assignment_ref import TrainComponentLabelAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentLabelAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment  of TRAIN COMPONENT NUMBER ASSIGNMENTs.
    """
    class Meta:
        name = "trainComponentLabelAssignments_RelStructure"

    train_component_label_assignment_ref_or_train_component_label_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainComponentLabelAssignmentRef",
                    "type": TrainComponentLabelAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentLabelAssignment",
                    "type": TrainComponentLabelAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
