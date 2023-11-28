from dataclasses import dataclass
from netex.access_vehicle_equipment_ref_structure import AccessVehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessVehicleEquipmentRef(AccessVehicleEquipmentRefStructure):
    """
    Reference to an ACCESS VEHICLE EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
