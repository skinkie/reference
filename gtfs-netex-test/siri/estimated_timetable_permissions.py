from dataclasses import dataclass, field
from typing import List

from .connection_service_permission_structure import ConnectionServicePermissionStructure
from .permissions_structure import PermissionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetablePermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    estimated_timetable_permission: List[ConnectionServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetablePermission",
            "type": "Element",
        },
    )
