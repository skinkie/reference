from dataclasses import dataclass
from netex.vehicle_requirement_ref_structure import VehicleRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleManoeuvringRequirementRefStructure(VehicleRequirementRefStructure):
    """
    Type for a reference to a VEHICLE REQUIREMENT.
    """
