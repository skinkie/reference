from dataclasses import dataclass
from netex.vehicle_model_profile_ref_structure import VehicleModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleModelProfileRefStructure(VehicleModelProfileRefStructure):
    """
    Type for a reference to a CYCLE MODEL PROFILE.
    """
