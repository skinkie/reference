from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .train_component_stop_assignment_ref import TrainComponentStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentStopAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "trainComponentStopAssignmentRefs_RelStructure"

    train_component_stop_assignment_ref: List[TrainComponentStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
