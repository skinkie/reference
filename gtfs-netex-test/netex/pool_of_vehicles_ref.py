from dataclasses import dataclass
from .pool_of_vehicles_ref_structure import PoolOfVehiclesRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoolOfVehiclesRef(PoolOfVehiclesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
