from dataclasses import dataclass

from .vehicle_requirement_ref_structure import VehicleRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirementRefStructure(VehicleRequirementRefStructure):
    pass
