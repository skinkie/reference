from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_entrance_assignments_rel_structure import DeckEntranceAssignment
from .dynamic_stop_assignment import DynamicStopAssignment
from .dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from .flexible_stop_assignment import FlexibleStopAssignment
from .navigation_path_assignment import NavigationPathAssignment
from .passenger_boarding_position_assignment import PassengerBoardingPositionAssignment
from .passenger_stop_assignment import PassengerStopAssignment
from .train_component_stop_assignment import TrainComponentStopAssignment
from .train_stop_assignment import TrainStopAssignment
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from .vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef
from .vehicle_type_stop_assignment import VehicleTypeStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyStopAssignments_RelStructure"

    vehicle_journey_stop_assignment_ref_or_stop_assignment_or_passenger_boarding_position_assignment: List[
        Union[
            DynamicStopAssignmentRef,
            VehicleJourneyStopAssignmentRef,
            DynamicStopAssignment,
            VehicleJourneyStopAssignment,
            VehicleTypeStopAssignment,
            FlexibleStopAssignment,
            NavigationPathAssignment,
            TrainStopAssignment,
            PassengerBoardingPositionAssignment,
            DeckEntranceAssignment,
            PassengerStopAssignment,
            TrainComponentStopAssignment,
        ]
    ] = field(
        default_factory=list,
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
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerBoardingPositionAssignment",
                    "type": PassengerBoardingPositionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckEntranceAssignment",
                    "type": DeckEntranceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentStopAssignment",
                    "type": TrainComponentStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
