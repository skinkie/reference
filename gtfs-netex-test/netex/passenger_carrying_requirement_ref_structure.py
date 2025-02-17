from dataclasses import dataclass

from .vehicle_requirement_ref_structure import VehicleRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerCarryingRequirementRefStructure(VehicleRequirementRefStructure):
    pass
