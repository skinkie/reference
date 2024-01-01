from dataclasses import dataclass
from .vehicle_charging_equipment_ref_structure import (
    VehicleChargingEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipmentRef(VehicleChargingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
