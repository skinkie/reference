from dataclasses import dataclass
from netex.vehicle_equipment_profile_ref_structure import VehicleEquipmentProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingEquipmentProfileRefStructure(VehicleEquipmentProfileRefStructure):
    """
    Type for a reference to an CHARGING EQUIPMENT PROFILE.
    """
