from dataclasses import dataclass, field
from typing import List, Optional, Union

from .boarding_position_ref_structure import BoardingPositionRefStructure
from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .entrance_setting_enumeration import EntranceSettingEnumeration
from .locatable_spot_range_ref_structure import LocatableSpotRangeRefStructure
from .multilingual_string import MultilingualString
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .passenger_entrance_ref import PassengerEntranceRef
from .passenger_stop_assignment_ref import PassengerStopAssignmentRef
from .powered_train_ref import PoweredTrainRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .train_component_ref import TrainComponentRef
from .train_component_view import TrainComponentView
from .train_ref import TrainRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckEntranceAssignments_RelStructure"

    deck_entrance_assignment: List["DeckEntranceAssignment"] = field(
        default_factory=list,
        metadata={
            "name": "DeckEntranceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PassengerBoardingPositionAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "PassengerBoardingPositionAssignment_VersionStructure"

    vehicle_journey_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[Union[DynamicStopAssignmentRef, VehicleJourneyStopAssignmentRef, PassengerStopAssignmentRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    train_component_ref_or_train_component_view: Optional[Union[TrainComponentRef, TrainComponentView]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentView",
                    "type": TrainComponentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    position_of_train_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "PositionOfTrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_ref: Optional[BoardingPositionRefStructure] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_allowed: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_to_vehicle: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_entrance_assignments: Optional[DeckEntranceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckEntranceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class DeckEntranceAssignmentVersionStructure(PassengerBoardingPositionAssignmentVersionStructure):
    class Meta:
        name = "DeckEntranceAssignment_VersionStructure"

    deck_entrance_ref: Optional[Union[OtherDeckEntranceRef, DeckVehicleEntranceRef, PassengerEntranceRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherDeckEntranceRef",
                    "type": OtherDeckEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckVehicleEntranceRef",
                    "type": DeckVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEntranceRef",
                    "type": PassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    entrance_setting: Optional[EntranceSettingEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceSetting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_spot: Optional[LocatableSpotRangeRefStructure] = field(
        default=None,
        metadata={
            "name": "StartSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_spot: List[LocatableSpotRangeRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "EndSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class DeckEntranceAssignment(DeckEntranceAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
