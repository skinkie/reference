from dataclasses import dataclass

from .vehicle_meeting_point_assignment_ref_structure import VehicleMeetingPointAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DynamicVehicleMeetingPointAssignmentRefStructure(VehicleMeetingPointAssignmentRefStructure):
    pass
