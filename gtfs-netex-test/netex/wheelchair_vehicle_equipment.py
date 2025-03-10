from dataclasses import dataclass

from .wheelchair_vehicle_equipment_version_structure import WheelchairVehicleEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WheelchairVehicleEquipment(WheelchairVehicleEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
