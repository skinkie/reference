from dataclasses import dataclass, field
from typing import Optional, Union

from .boarding_position_ref_structure import BoardingPositionRefStructure
from .deck_entrance_assignments_rel_structure import DeckEntranceAssignmentsRelStructure
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .multilingual_string import MultilingualString
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
class TrainStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "TrainStopAssignment_VersionStructure"

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
    is_allowed: Optional[bool] = field(
        default=None,
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
