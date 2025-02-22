from dataclasses import dataclass

from .vehicle_type_at_point_version_structure import VehicleTypeAtPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleTypeAtPoint(VehicleTypeAtPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
