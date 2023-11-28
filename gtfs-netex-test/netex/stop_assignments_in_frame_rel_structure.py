from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dynamic_stop_assignment import DynamicStopAssignment
from netex.flexible_stop_assignment import FlexibleStopAssignment
from netex.navigation_path_assignment import NavigationPathAssignment
from netex.passenger_stop_assignment import PassengerStopAssignment
from netex.train_stop_assignment import TrainStopAssignment
from netex.vehicle_journey_stop_assignment import VehicleJourneyStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of STOP ASSIGNMENTs.
    """
    class Meta:
        name = "stopAssignmentsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
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
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
