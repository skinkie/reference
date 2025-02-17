from dataclasses import dataclass

from .battery_equipment_version_structure import BatteryEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BatteryEquipment(BatteryEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
