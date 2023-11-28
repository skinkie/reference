from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dynamic_vehicle_meeting_point_assignment_ref import DynamicVehicleMeetingPointAssignmentRef
from netex.vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1
from netex.vehicle_meeting_point_assignment_ref import VehicleMeetingPointAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE MEETING POINT ASSIGNMENT.
    """
    class Meta:
        name = "vehicleMeetingPointAssignments_RelStructure"

    dynamic_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DynamicVehicleMeetingPointAssignmentRef",
                    "type": DynamicVehicleMeetingPointAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignmentRef",
                    "type": VehicleMeetingPointAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointAssignment",
                    "type": VehicleMeetingPointAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
