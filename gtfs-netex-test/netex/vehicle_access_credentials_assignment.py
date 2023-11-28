from dataclasses import dataclass, field
from netex.vehicle_access_credentials_assignment_version_structure import VehicleAccessCredentialsAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleAccessCredentialsAssignment(VehicleAccessCredentialsAssignmentVersionStructure):
    """The allocation of a MEDIUM ACCESS DEVICE to a specific VEHICLE, to allow the
    user (TRANSPORT CUSTOMER) to access the vehicle (tyically for VEHICLE SHARING
    or VEHICLE RENTAL).

    This allocation may have validity limitations. +V1.2.2

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
