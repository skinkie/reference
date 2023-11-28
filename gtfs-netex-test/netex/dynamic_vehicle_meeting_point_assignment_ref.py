from dataclasses import dataclass
from netex.dynamic_vehicle_meeting_point_assignment_ref_structure import DynamicVehicleMeetingPointAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicVehicleMeetingPointAssignmentRef(DynamicVehicleMeetingPointAssignmentRefStructure):
    """Reference to a DYNAMIC VEHICLE MEETING POINT ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
