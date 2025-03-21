from dataclasses import dataclass

from .vehicle_equipment_profile_ref_structure import VehicleEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingEquipmentProfileRefStructure(VehicleEquipmentProfileRefStructure):
    pass
