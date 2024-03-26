from dataclasses import dataclass

from .cycle_storage_equipment_version_structure import (
    CycleStorageEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CycleStorageEquipment(CycleStorageEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
