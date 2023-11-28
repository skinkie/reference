from dataclasses import dataclass, field
from netex.all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoadVehicleMode:
    """Road Vehicle MODE: a characterisation of the operation according to the means of transport (bus, tram, coach)."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration = field(
        metadata={
            "required": True,
        }
    )
