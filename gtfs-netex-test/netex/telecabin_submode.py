from dataclasses import dataclass, field

from .telecabin_submode_enumeration import TelecabinSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TelecabinSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TelecabinSubmodeEnumeration = field(
        default=TelecabinSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
