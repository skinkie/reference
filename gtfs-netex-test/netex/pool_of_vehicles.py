from dataclasses import dataclass

from .pool_of_vehicles_version_structure import PoolOfVehiclesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoolOfVehicles(PoolOfVehiclesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
