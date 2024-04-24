from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from .derived_view_structure import DerivedViewStructure
from .fare_classes import FareClasses
from .multilingual_string import MultilingualString
from .tractive_element_type_ref import TractiveElementTypeRef
from .trailing_element_type_ref import TrailingElementTypeRef
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_element_type_ref import TrainElementTypeRef
from .train_element_type_type_enumeration import TrainElementTypeTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "TrainComponent_DerivedViewStructure"

    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trailing_element_type_ref_or_tractive_element_type_ref_or_train_element_type_ref_or_train_element_ref: Optional[Union[TrailingElementTypeRef, TractiveElementTypeRef, TrainElementTypeRef, TrainElementRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrailingElementTypeRef",
                    "type": TrailingElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveElementTypeRef",
                    "type": TractiveElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementTypeRef",
                    "type": TrainElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fare_classes: Optional[FareClasses] = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_type_type_or_train_element_type: Optional[Union["TrainComponentDerivedViewStructure.TrainElementTypeType", "TrainComponentDerivedViewStructure.TrainElementType"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElementTypeType",
                    "type": ForwardRef("TrainComponentDerivedViewStructure.TrainElementTypeType"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementType",
                    "type": ForwardRef("TrainComponentDerivedViewStructure.TrainElementType"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class TrainElementTypeType:
        value: TrainElementTypeTypeEnumeration = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TrainElementType:
        value: TrainElementTypeTypeEnumeration = field(
            metadata={
                "required": True,
            }
        )
