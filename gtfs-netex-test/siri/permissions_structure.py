from dataclasses import dataclass, field
from typing import Optional

from .version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PermissionsStructure:
    permission_version_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "PermissionVersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
