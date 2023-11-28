from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.train_component import TrainComponent
from netex.train_component_ref import TrainComponentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TRAIN COMPONENTs.
    """
    class Meta:
        name = "trainComponents_RelStructure"

    train_component_ref_or_train_component: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponent",
                    "type": TrainComponent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
