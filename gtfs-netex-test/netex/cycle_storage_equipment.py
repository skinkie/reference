from dataclasses import dataclass, field
from netex.cycle_storage_equipment_version_structure import CycleStorageEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleStorageEquipment(CycleStorageEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for cycle storage.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
