from dataclasses import dataclass, field
from netex.boarding_permission_enumeration import BoardingPermissionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BoardingPermission:
    """Classification of BOARDING PERMISSION - UIC 7161 Code list."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BoardingPermissionEnumeration = field(
        metadata={
            "required": True,
        }
    )
