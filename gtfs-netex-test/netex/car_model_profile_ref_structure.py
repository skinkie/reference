from dataclasses import dataclass

from .vehicle_model_profile_ref_structure import VehicleModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarModelProfileRefStructure(VehicleModelProfileRefStructure):
    pass
