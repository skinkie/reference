from dataclasses import dataclass

from .equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BatteryEquipmentRefStructure(EquipmentRefStructure):
    pass
