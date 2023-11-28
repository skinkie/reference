from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_journey_stop_assignment import VehicleJourneyStopAssignment
from netex.vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyStopAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment of VEHICLE JOURNEY STOP ASSIGNMENTs.
    """
    class Meta:
        name = "vehicleJourneyStopAssignments_RelStructure"

    vehicle_journey_stop_assignment_ref_or_vehicle_journey_stop_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
