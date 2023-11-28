from dataclasses import dataclass
from netex.battery_equipment_ref_structure import BatteryEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BatteryEquipmentRef(BatteryEquipmentRefStructure):
    """Identifier of an BATTERY EQUIPMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
