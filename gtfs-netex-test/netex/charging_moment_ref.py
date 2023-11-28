from dataclasses import dataclass
from netex.charging_moment_ref_structure import ChargingMomentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingMomentRef(ChargingMomentRefStructure):
    """Reference to a CHARGING MOMENT.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
