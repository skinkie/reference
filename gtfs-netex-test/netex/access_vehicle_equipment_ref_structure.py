from dataclasses import dataclass
from netex.vehicle_equipment_ref_structure import VehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessVehicleEquipmentRefStructure(VehicleEquipmentRefStructure):
    """
    Type for a reference to an ACCESS VEHICLE EQUIPMENT.
    """
