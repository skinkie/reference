from dataclasses import dataclass, field
from netex.metro_submode_enumeration import MetroSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MetroSubmode:
    """
    TPEG pti04 Metro submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MetroSubmodeEnumeration = field(
        default=MetroSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
