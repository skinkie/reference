from dataclasses import dataclass
from netex.charging_equipment_profile_ref_structure import ChargingEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingEquipmentProfileRef(ChargingEquipmentProfileRefStructure):
    """Identifier of an CHARGING EQUIPMENT PROFILE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
