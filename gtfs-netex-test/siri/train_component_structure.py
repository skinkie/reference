from dataclasses import dataclass, field
from typing import Optional, Union

from .natural_language_string_structure import NaturalLanguageStringStructure
from .train_element import TrainElement
from .train_element_ref import TrainElementRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainComponentStructure:
    train_component_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainComponentCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: int = field(
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    label: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_element_ref_or_train_element: Optional[Union[TrainElementRef, TrainElement]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
