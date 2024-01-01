from dataclasses import dataclass, field
from .boarding_permission_enumeration import BoardingPermissionEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPermission:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BoardingPermissionEnumeration = field(
        metadata={
            "required": True,
        }
    )
