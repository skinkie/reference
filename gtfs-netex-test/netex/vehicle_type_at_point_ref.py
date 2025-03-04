from dataclasses import dataclass

from .vehicle_type_at_point_ref_structure import VehicleTypeAtPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleTypeAtPointRef(VehicleTypeAtPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
