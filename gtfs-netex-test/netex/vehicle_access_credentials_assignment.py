from dataclasses import dataclass
from .vehicle_access_credentials_assignment_version_structure import (
    VehicleAccessCredentialsAssignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessCredentialsAssignment(
    VehicleAccessCredentialsAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
