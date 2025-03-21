from dataclasses import dataclass, field
from typing import Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .powered_train_ref import PoweredTrainRef
from .train import Train
from .train_ref import TrainRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainInCompoundTrainVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "TrainInCompoundTrain_VersionedChildStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    unpowered_train_ref_or_powered_train_ref_or_train_ref_or_train: Optional[Union[UnpoweredTrainRef, PoweredTrainRef, TrainRef, Train]] = field(
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
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    operational_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "OperationalOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
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
