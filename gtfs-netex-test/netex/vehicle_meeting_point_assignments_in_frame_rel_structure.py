from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_point_assignment_1 import VehicleMeetingPointAssignment1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE MEETING POINT ASSIGNMENT.
    """
    class Meta:
        name = "vehicleMeetingPointAssignmentsInFrame_RelStructure"

    vehicle_meeting_point_assignment: List[VehicleMeetingPointAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
