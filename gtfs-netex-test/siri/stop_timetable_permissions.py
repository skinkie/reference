from dataclasses import dataclass, field
from typing import List

from .permissions_structure import PermissionsStructure
from .stop_timetable_service_permission_structure import StopTimetableServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetablePermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    stop_timetable_permission: List[StopTimetableServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetablePermission",
            "type": "Element",
        },
    )
