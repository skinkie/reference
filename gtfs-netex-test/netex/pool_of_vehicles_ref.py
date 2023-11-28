from dataclasses import dataclass
from netex.pool_of_vehicles_ref_structure import PoolOfVehiclesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PoolOfVehiclesRef(PoolOfVehiclesRefStructure):
    """Reference to an POOL OF VEHICLEs.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
