from dataclasses import dataclass

from .vehicle_equipment_ref_structure import VehicleEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WheelchairVehicleEquipmentRefStructure(VehicleEquipmentRefStructure):
    pass
