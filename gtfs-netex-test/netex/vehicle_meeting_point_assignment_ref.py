from dataclasses import dataclass
from netex.vehicle_meeting_point_assignment_ref_structure import VehicleMeetingPointAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentRef(VehicleMeetingPointAssignmentRefStructure):
    """Reference to a VEHICLE MEETING POINT ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
