from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_component_stop_assignment import TrainComponentStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainComponentStopAssignments_RelStructure"

    train_component_stop_assignment: List[TrainComponentStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
