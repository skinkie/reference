from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_component import TrainComponent
from .train_component_ref import TrainComponentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainComponentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainComponents_RelStructure"

    train_component_ref_or_train_component: list[Union[TrainComponentRef, TrainComponent]] = field(
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
        },
    )
