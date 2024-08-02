from dataclasses import dataclass, field
from typing import List

from .facility_monitoring_service_permission_structure import FacilityMonitoringServicePermissionStructure
from .permissions_structure import PermissionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringPermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    facility_monitoring_permission: List[FacilityMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringPermission",
            "type": "Element",
        },
    )
