from dataclasses import dataclass
from netex.vehicle_profile_ref_structure import VehicleProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleProfileRef(VehicleProfileRefStructure):
    """
    Reference to a VEHICLE PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
