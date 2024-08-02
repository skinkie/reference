from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_permission_structure import AbstractPermissionStructure
from .allow_all import AllowAll
from .extensions_1 import Extensions1
from .line_permissions import LinePermissions
from .operator_permissions import OperatorPermissions
from .stop_monitor_permission_structure import StopMonitorPermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringServicePermissionStructure(AbstractPermissionStructure):
    operator_permissions: OperatorPermissions = field(
        metadata={
            "name": "OperatorPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    line_permissions: LinePermissions = field(
        metadata={
            "name": "LinePermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_monitor_permissions: "StopMonitoringServicePermissionStructure.StopMonitorPermissions" = field(
        metadata={
            "name": "StopMonitorPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class StopMonitorPermissions:
        allow_all_or_stop_monitor_permission: List[Union[AllowAll, StopMonitorPermissionStructure]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "AllowAll",
                        "type": AllowAll,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "StopMonitorPermission",
                        "type": StopMonitorPermissionStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
