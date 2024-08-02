from dataclasses import dataclass, field
from typing import List

from .general_message_service_permission_structure import GeneralMessageServicePermissionStructure
from .permissions_structure import PermissionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessagePermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    general_message_permission: List[GeneralMessageServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessagePermission",
            "type": "Element",
        },
    )
