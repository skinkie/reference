from dataclasses import dataclass

from .vehicle_access_credentials_assignment_ref_structure import VehicleAccessCredentialsAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleAccessCredentialsAssignmentRef(VehicleAccessCredentialsAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
