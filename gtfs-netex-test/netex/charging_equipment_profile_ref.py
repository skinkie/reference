from dataclasses import dataclass
from .charging_equipment_profile_ref_structure import (
    ChargingEquipmentProfileRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingEquipmentProfileRef(ChargingEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
