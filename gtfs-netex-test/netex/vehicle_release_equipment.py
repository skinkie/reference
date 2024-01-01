from dataclasses import dataclass
from .vehicle_release_equipment_version_structure import (
    VehicleReleaseEquipmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleReleaseEquipment(VehicleReleaseEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
