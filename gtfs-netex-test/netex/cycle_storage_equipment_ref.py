from dataclasses import dataclass
from netex.cycle_storage_equipment_ref_structure import CycleStorageEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleStorageEquipmentRef(CycleStorageEquipmentRefStructure):
    """
    Identifier of an CYCLE STORAGE EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
