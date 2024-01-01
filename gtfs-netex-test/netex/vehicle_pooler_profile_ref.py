from dataclasses import dataclass
from .vehicle_pooler_profile_ref_structure import (
    VehiclePoolerProfileRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolerProfileRef(VehiclePoolerProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
