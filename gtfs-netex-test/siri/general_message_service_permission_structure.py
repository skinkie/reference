from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_permission_structure import AbstractPermissionStructure
from .allow_all import AllowAll
from .extensions_1 import Extensions1
from .info_channel_permission_structure import InfoChannelPermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageServicePermissionStructure(AbstractPermissionStructure):
    info_channel_permissions: "GeneralMessageServicePermissionStructure.InfoChannelPermissions" = field(
        metadata={
            "name": "InfoChannelPermissions",
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
    class InfoChannelPermissions:
        allow_all_or_info_channel_permission: List[Union[AllowAll, InfoChannelPermissionStructure]] = field(
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
                        "name": "InfoChannelPermission",
                        "type": InfoChannelPermissionStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
