from dataclasses import dataclass

from .vehicle_service_part_ref_structure import VehicleServicePartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleServicePartRef(VehicleServicePartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
