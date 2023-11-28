from dataclasses import dataclass, field
from netex.air_submode_enumeration import AirSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AirSubmode:
    """
    TPEG pti08 Air submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AirSubmodeEnumeration = field(
        default=AirSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
