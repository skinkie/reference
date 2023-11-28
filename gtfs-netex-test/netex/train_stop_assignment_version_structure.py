from dataclasses import dataclass, field
from typing import Optional
from netex.boarding_position_ref_structure import BoardingPositionRefStructure
from netex.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from netex.multilingual_string import MultilingualString
from netex.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from netex.stop_assignment_version_structure import StopAssignmentVersionStructure
from netex.train_component_ref import TrainComponentRef
from netex.train_component_view import TrainComponentView
from netex.train_ref import TrainRef
from netex.vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a TRAIN STOP POINT ASSIGNMENT.

    :ivar
        vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref:
    :ivar train_ref:
    :ivar train_component_ref_or_train_component_view:
    :ivar position_of_train_element: Relative position of TRAIN ELEMENT.
    :ivar boarding_position_ref: BOARDING POSITION to which SCHEDULED
        STOP POINT is to be assigned.
    :ivar entrance_to_vehicle: A specific ENTRANCE to the VEHICLE. E.g.
        Front, rear.
    """
    class Meta:
        name = "TrainStopAssignment_VersionStructure"

    vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    train_component_ref_or_train_component_view: Optional[object] = field(
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
        }
    )
    position_of_train_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "PositionOfTrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRefStructure] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_to_vehicle: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
