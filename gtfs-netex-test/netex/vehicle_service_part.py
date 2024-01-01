from dataclasses import dataclass
from .vehicle_service_part_version_structure import (
    VehicleServicePartVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServicePart(VehicleServicePartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
