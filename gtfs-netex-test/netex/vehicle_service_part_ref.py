from dataclasses import dataclass
from .vehicle_service_part_ref_structure import VehicleServicePartRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePartRef(VehicleServicePartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
