from dataclasses import dataclass

from .vehicle_model_ref_structure import VehicleModelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleModelRef(VehicleModelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
