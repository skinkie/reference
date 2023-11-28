from dataclasses import dataclass, field
from typing import Optional
from netex.dynamic_vehicle_meeting_point_assignment_ref import DynamicVehicleMeetingPointAssignmentRef
from netex.vehicle_meeting_point_assignment_ref import VehicleMeetingPointAssignmentRef
from netex.vehicle_meeting_point_assignment_version_structure import VehicleMeetingPointAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicVehicleMeetingPointAssignmentVersionStructure(VehicleMeetingPointAssignmentVersionStructure):
    """
    Type for DYNAMIC VEHICLE MEETING POINT ASSIGNMENT restricts id.
    """
    class Meta:
        name = "DynamicVehicleMeetingPointAssignment_VersionStructure"

    dynamic_vehicle_meeting_point_assignment_ref_or_vehicle_meeting_point_assignment_ref: Optional[object] = field(
        default=None,
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
            ),
        }
    )
