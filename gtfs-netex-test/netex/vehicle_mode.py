from dataclasses import dataclass, field
from netex.all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMode:
    """VEHICLE MODE: a characterisation of the operation according to the means of transport (bus, tram, metro, train, ferry, ship)."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration = field(
        metadata={
            "required": True,
        }
    )
