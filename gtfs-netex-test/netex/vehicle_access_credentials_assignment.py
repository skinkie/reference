from dataclasses import dataclass

from .vehicle_access_credentials_assignment_version_structure import VehicleAccessCredentialsAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleAccessCredentialsAssignment(VehicleAccessCredentialsAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
