from dataclasses import dataclass, field
from typing import List

from .connection_service_permission_structure import ConnectionServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringPermissions:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    connection_monitoring_permission: List[ConnectionServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringPermission",
            "type": "Element",
        },
    )
