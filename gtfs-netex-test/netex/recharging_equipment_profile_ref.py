from dataclasses import dataclass

from .recharging_equipment_profile_ref_structure import RechargingEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingEquipmentProfileRef(RechargingEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
