from dataclasses import dataclass, field
from typing import List, Union

from .allow_all import AllowAll
from .line_permission_structure import LinePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LinePermissions:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all_or_line_permission: List[Union[AllowAll, LinePermissionStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllowAll",
                    "type": AllowAll,
                },
                {
                    "name": "LinePermission",
                    "type": LinePermissionStructure,
                },
            ),
        },
    )
