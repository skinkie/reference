from dataclasses import dataclass
from netex.vehicle_pooler_profile_ref_structure import VehiclePoolerProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolerProfileRef(VehiclePoolerProfileRefStructure):
    """Reference to a VEHICLE POOLER PROFILE usage parameter.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
