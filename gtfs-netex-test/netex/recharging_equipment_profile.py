from dataclasses import dataclass

from .recharging_equipment_profile_version_structure import (
    RechargingEquipmentProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingEquipmentProfile(RechargingEquipmentProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
