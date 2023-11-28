from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.compound_train_ref import CompoundTrainRef
from netex.multilingual_string import MultilingualString
from netex.train import Train
from netex.train_ref import TrainRef
from netex.vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainInCompoundTrainVersionedChildStructure(VersionedChildStructure):
    """
    Type for a TRAIN IN COMPOUND TRAIN.

    :ivar description: Description of TRAIN IN COMPOUND TRAIN.
    :ivar compound_train_ref: Reference to a TRAIN ELEMENT.
    :ivar train_ref_or_train:
    :ivar label: Label for TRAIN IN COMPOUND TRAIN.
    :ivar operational_orientation: Orientation of the  TRAIN IN COMPOUND
        TRAIN
    :ivar reversed_orientation: Whether the component order of the TRAIN
        IN COMPOUND TRAIN is reversed compared to the order in the
        TRAIN.
    :ivar order: Order of TRAIN IN COMPOUND TRAIN within TRAIN.
    """
    class Meta:
        name = "TrainInCompoundTrain_VersionedChildStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_ref_or_train: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "OperationalOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
