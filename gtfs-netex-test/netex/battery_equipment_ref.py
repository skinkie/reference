from dataclasses import dataclass
from .battery_equipment_ref_structure import BatteryEquipmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BatteryEquipmentRef(BatteryEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
