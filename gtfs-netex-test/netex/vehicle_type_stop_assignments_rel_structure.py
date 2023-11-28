from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_type_stop_assignment import VehicleTypeStopAssignment
from netex.vehicle_type_stop_assignment_ref import VehicleTypeStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeStopAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment  of  VEHICLE TYPE STOP ASSIGNNMENTs.
    """
    class Meta:
        name = "vehicleTypeStopAssignments_RelStructure"

    vehicle_type_stop_assignment_ref_or_vehicle_type_stop_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleTypeStopAssignmentRef",
                    "type": VehicleTypeStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
