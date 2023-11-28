from dataclasses import dataclass, field
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SnowAndIceSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SnowAndIceSubmodeEnumeration = field(
        default=SnowAndIceSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
