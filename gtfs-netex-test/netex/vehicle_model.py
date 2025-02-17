from dataclasses import dataclass

from .vehicle_model_version_structure import VehicleModelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleModel(VehicleModelVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
