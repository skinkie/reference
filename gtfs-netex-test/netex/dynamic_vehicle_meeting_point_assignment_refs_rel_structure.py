from dataclasses import dataclass, field
from netex.dynamic_vehicle_meeting_point_assignment_ref import DynamicVehicleMeetingPointAssignmentRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DynamicVehicleMeetingPointAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of DYNAMIC VEHICLE MEETING POINT ASSIGNMENTs.
    """
    class Meta:
        name = "dynamicVehicleMeetingPointAssignmentRefs_RelStructure"

    dynamic_vehicle_meeting_point_assignment_ref: DynamicVehicleMeetingPointAssignmentRef = field(
        metadata={
            "name": "DynamicVehicleMeetingPointAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
