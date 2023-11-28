from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_sharing_place_assignment_ref import VehicleSharingPlaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingPlaceAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of VEHICLE SHARING PLACE ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "VehicleSharingPlaceAssignmentRefs_RelStructure"

    vehicle_sharing_place_assignment_ref: VehicleSharingPlaceAssignmentRef = field(
        metadata={
            "name": "VehicleSharingPlaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
