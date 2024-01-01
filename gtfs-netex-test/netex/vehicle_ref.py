from dataclasses import dataclass
from .vehicle_ref_structure import VehicleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRef(VehicleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
