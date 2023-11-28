from dataclasses import dataclass, field
from netex.access_mode_enumeration import AccessModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessMode:
    """
    Access MODE for SITEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccessModeEnumeration = field(
        metadata={
            "required": True,
        }
    )
