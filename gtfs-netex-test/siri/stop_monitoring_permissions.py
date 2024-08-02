from dataclasses import dataclass, field
from typing import List

from .permissions_structure import PermissionsStructure
from .stop_monitoring_service_permission_structure import StopMonitoringServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringPermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    stop_monitoring_permission: List[StopMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringPermission",
            "type": "Element",
        },
    )
