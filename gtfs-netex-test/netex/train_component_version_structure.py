from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.train_element import TrainElement
from netex.train_element_ref import TrainElementRef
from netex.train_ref import TrainRef
from netex.vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentVersionStructure(DataManagedObjectStructure):
    """
    Type for a TRAIN COMPONENT.

    :ivar label: Label for TRAIN COMPONENT.
    :ivar description: Description of TRAIN COMPONENT.
    :ivar train_ref: Reference to a TRAIN.
    :ivar train_element_ref_or_train_element:
    :ivar operational_orientation: Orientation of the  TRAIN ELEMENT
        within the TRAIN. +v1.1.
    :ivar order: Order of TRAIN COMPONENT within TRAIN.
    """
    class Meta:
        name = "TrainComponent_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_element_ref_or_train_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
