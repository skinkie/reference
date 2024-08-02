from dataclasses import dataclass, field
from typing import List, Union

from .allow_all import AllowAll
from .connection_link_permission_structure import ConnectionLinkPermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinkPermissions:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all_or_connection_link_permission: List[Union[AllowAll, ConnectionLinkPermissionStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowAll",
                    "type": AllowAll,
                },
                {
                    "name": "ConnectionLinkPermission",
                    "type": ConnectionLinkPermissionStructure,
                },
            ),
        },
    )
