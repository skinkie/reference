from dataclasses import dataclass
from .vehicle_type_version_structure import VehicleTypeVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleType(VehicleTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
