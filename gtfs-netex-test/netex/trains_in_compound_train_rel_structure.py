from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.train_in_compound_train_versioned_child_structure import TrainInCompoundTrainVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainsInCompoundTrainRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of TRAIN IN COMPOUND TRAIN.

    :ivar train_in_compound_train: An instance of a TRAIN making up a
        COMPOUND TRAIN.
    """
    class Meta:
        name = "trainsInCompoundTrain_RelStructure"

    train_in_compound_train: List[TrainInCompoundTrainVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainInCompoundTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
