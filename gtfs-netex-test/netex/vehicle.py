from dataclasses import dataclass
from .vehicle_version_structure import VehicleVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Vehicle(VehicleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
