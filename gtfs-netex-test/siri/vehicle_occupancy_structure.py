from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from .compound_train_ref import CompoundTrainRef
from .entrance_to_vehicle_ref import EntranceToVehicleRef
from .fare_class_enumeration import FareClassEnumeration
from .group_reservation_structure import GroupReservationStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .occupancy_enumeration import OccupancyEnumeration
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_ref import TrainRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleOccupancyStructure:
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
    occupancy_level: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "OccupancyLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OccupancyPercentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("0"),
        },
    )
    alighting_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AlightingCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BoardingCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "OnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    special_places_occupied: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlacesOccupied",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pushchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    wheelchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prams_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bicycle_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    total_number_of_reserved_seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_reservation: List[GroupReservationStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupReservation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
