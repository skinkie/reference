from dataclasses import dataclass

from .vehicle_pooler_profile_ref_structure import VehiclePoolerProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolerProfileRef(VehiclePoolerProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
