from dataclasses import dataclass, field
from typing import Optional, Union

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .powered_train_ref import PoweredTrainRef
from .tractive_element_type_ref import TractiveElementTypeRef
from .trailing_element_type_ref import TrailingElementTypeRef
from .train_component_coupling_structure import TrainComponentCouplingStructure
from .train_element import TrainElement
from .train_element_ref import TrainElementRef
from .train_element_type_ref import TrainElementTypeRef
from .train_ref import TrainRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainComponent_VersionStructure"

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
    train_ref: Optional[Union[UnpoweredTrainRef, PoweredTrainRef, TrainRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnpoweredTrainRef",
                    "type": UnpoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrainRef",
                    "type": PoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    trailing_element_type_ref_or_tractive_element_type_ref_or_train_element_type_ref_or_train_element_ref_or_train_element: Optional[Union[TrailingElementTypeRef, TractiveElementTypeRef, TrainElementTypeRef, TrainElementRef, TrainElement]] = field(
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
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    operational_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "OperationalOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    forward_coupling: Optional[TrainComponentCouplingStructure] = field(
        default=None,
        metadata={
            "name": "ForwardCoupling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
