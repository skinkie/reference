from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .tractive_element_type import TractiveElementType
from .trailing_element_type import TrailingElementType
from .train_element import TrainElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElementTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainElementTypesInFrame_RelStructure"

    trailing_element_type_or_tractive_element_type_or_train_element: List[Union[TrailingElementType, TractiveElementType, TrainElement]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrailingElementType",
                    "type": TrailingElementType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveElementType",
                    "type": TractiveElementType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
