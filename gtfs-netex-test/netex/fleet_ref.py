from dataclasses import dataclass
from netex.fleet_ref_structure import FleetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FleetRef(FleetRefStructure):
    """Reference to a FLEET.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
