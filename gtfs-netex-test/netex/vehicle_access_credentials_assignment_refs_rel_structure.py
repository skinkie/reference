from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_access_credentials_assignment_ref import VehicleAccessCredentialsAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleAccessCredentialsAssignmentRefsRelStructure(OneToManyRelationshipStructure):
    """Type for a list of VEHICLE ACCESS CREDENTIALS ASSIGNMENTs.

    +v1.2.2
    """
    class Meta:
        name = "vehicleAccessCredentialsAssignmentRefs_RelStructure"

    vehicle_access_credentials_assignment_ref: VehicleAccessCredentialsAssignmentRef = field(
        metadata={
            "name": "VehicleAccessCredentialsAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
