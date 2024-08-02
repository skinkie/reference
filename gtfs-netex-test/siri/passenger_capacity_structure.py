from dataclasses import dataclass, field
from typing import Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entrance_to_vehicle_ref import EntranceToVehicleRef
from .fare_class_enumeration import FareClassEnumeration
from .natural_language_string_structure import NaturalLanguageStringStructure
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_ref import TrainRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassengerCapacityStructure:
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_ref_or_train_in_compound_train_ref: Optional[Union[TrainRef, TrainInCompoundTrainRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainInCompoundTrainRef",
                    "type": TrainInCompoundTrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    train_element_ref_or_train_component_ref: Optional[Union[TrainElementRef, TrainComponentRef]] = field(
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
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    entrance_to_vehicle_ref: Optional[EntranceToVehicleRef] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_category: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    seating_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatingCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standing_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    special_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pushchair_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    wheelchair_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pram_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bicycle_rack_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleRackCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
