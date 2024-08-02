from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    DayTypesRelStructure,
)
from .fare_class_enumeration import FareClassEnumeration
from .group_reservation_structure import GroupReservationStructure
from .multilingual_string import MultilingualString
from .natural_language_string_structure import NaturalLanguageStringStructure
from .occupancy_enumeration import OccupancyEnumeration
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
class OccupancyViewVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OccupancyView_VersionStructure"

    day_type_refs: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypeRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
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
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_category: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    occupancy_level: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "OccupancyLevel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    occupancy_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OccupancyPercentage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AlightingCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BoardingCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "OnboardCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    special_places_occupied: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlacesOccupied",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pushchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prams_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramsOnboardCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bicycle_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleOnboardCount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_number_of_reserved_seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_reservation: List[GroupReservationStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
