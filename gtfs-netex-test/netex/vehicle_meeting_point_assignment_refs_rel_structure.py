from dataclasses import dataclass, field
from typing import Optional
from netex.dynamic_vehicle_meeting_point_assignment_ref import DynamicVehicleMeetingPointAssignmentRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_meeting_point_assignment_ref import VehicleMeetingPointAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE MEETING POINT ASSIGNMENTs.
    """
    class Meta:
        name = "vehicleMeetingPointAssignmentRefs_RelStructure"

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
