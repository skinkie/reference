from dataclasses import dataclass
from netex.vehicle_meeting_point_assignment_ref_structure import VehicleMeetingPointAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicVehicleMeetingPointAssignmentRefStructure(VehicleMeetingPointAssignmentRefStructure):
    """
    Type for a reference to a DYNAMIC VEHICLE MEETING POINT ASSIGNMENT.
    """
