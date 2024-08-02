from dataclasses import dataclass, field
from typing import List, Union

from .allow_all import AllowAll
from .operator_permission_structure import OperatorPermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OperatorPermissions:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all_or_operator_permission: List[Union[AllowAll, OperatorPermissionStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowAll",
                    "type": AllowAll,
                },
                {
                    "name": "OperatorPermission",
                    "type": OperatorPermissionStructure,
                },
            ),
        },
    )
