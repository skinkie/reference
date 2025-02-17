from dataclasses import dataclass, field

from .all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration = field(
        metadata={
            "required": True,
        }
    )
