from dataclasses import dataclass
from .vehicle_equipment_profile_ref_structure import (
    VehicleEquipmentProfileRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingEquipmentProfileRefStructure(
    VehicleEquipmentProfileRefStructure
):
    value: RestrictedVar
