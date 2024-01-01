from dataclasses import dataclass
from .vehicle_release_equipment_ref_structure import (
    VehicleReleaseEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleReleaseEquipmentRef(VehicleReleaseEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
