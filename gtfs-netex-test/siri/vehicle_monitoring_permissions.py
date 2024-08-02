from dataclasses import dataclass, field
from typing import List

from .permissions_structure import PermissionsStructure
from .vehicle_monitoring_service_permission_structure import VehicleMonitoringServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringPermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    vehicle_monitoring_permission: List[VehicleMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringPermission",
            "type": "Element",
        },
    )
