from dataclasses import dataclass, field
from netex.vehicle_meeting_point_assignment_version_structure import VehicleMeetingPointAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignment1(VehicleMeetingPointAssignmentVersionStructure):
    """The allocation of a VEHICLE MEETING POINT to a SITE COMPONENT or ADDRESSABLE
    PLACE (for vehicle pooling or vehicle sharing purposes).

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        name = "VehicleMeetingPointAssignment"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
