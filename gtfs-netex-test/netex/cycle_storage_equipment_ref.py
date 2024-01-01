from dataclasses import dataclass
from .cycle_storage_equipment_ref_structure import (
    CycleStorageEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CycleStorageEquipmentRef(CycleStorageEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
