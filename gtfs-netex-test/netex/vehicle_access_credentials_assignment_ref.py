from dataclasses import dataclass
from netex.vehicle_access_credentials_assignment_ref_structure import VehicleAccessCredentialsAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleAccessCredentialsAssignmentRef(VehicleAccessCredentialsAssignmentRefStructure):
    """Reference to a VEHICLE ACCESS CREDENTIALS ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
