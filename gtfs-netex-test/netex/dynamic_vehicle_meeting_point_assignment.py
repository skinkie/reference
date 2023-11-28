from dataclasses import dataclass, field
from netex.dynamic_vehicle_meeting_point_assignment_version_structure import DynamicVehicleMeetingPointAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicVehicleMeetingPointAssignment(DynamicVehicleMeetingPointAssignmentVersionStructure):
    """Dynamic allocation of a VEHICLE MEETING ASSIGNMENT.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
