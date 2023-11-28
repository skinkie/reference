from dataclasses import dataclass, field
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TelecabinSubmode:
    """
    TPEG pti09 Telecabin submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TelecabinSubmodeEnumeration = field(
        default=TelecabinSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
