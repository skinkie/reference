from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .connection_service_permission_structure import ConnectionServicePermissionStructure
from .connection_timetable_service_capabilities import ConnectionTimetableServiceCapabilities
from .extensions_1 import Extensions1
from .permissions_structure import PermissionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    connection_timetable_service_capabilities: Optional[ConnectionTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_permissions: Optional["ConnectionTimetableCapabilitiesResponseStructure.ConnectionTimetablePermissions"] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetablePermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ConnectionTimetablePermissions(PermissionsStructure):
        connection_timetable_permission: List[ConnectionServicePermissionStructure] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionTimetablePermission",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
