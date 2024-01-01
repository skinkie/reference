from dataclasses import dataclass
from .vehicle_pooler_profile_version_structure import (
    VehiclePoolerProfileVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolerProfile(VehiclePoolerProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
