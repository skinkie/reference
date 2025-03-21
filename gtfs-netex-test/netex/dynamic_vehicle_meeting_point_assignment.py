from dataclasses import dataclass

from .dynamic_vehicle_meeting_point_assignment_version_structure import DynamicVehicleMeetingPointAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DynamicVehicleMeetingPointAssignment(DynamicVehicleMeetingPointAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
