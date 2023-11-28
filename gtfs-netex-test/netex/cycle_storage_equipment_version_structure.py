from dataclasses import dataclass, field
from typing import Optional
from netex.cycle_storage_enumeration import CycleStorageEnumeration
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleStorageEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a CYCLE STORAGE EQUIPMENT.

    :ivar number_of_spaces: Number of spaces available.
    :ivar cycle_storage_type: Type of storage.
    :ivar cage: whether shelter is enclosed.
    :ivar covered: Whether storage is covered.
    """
    class Meta:
        name = "CycleStorageEquipment_VersionStructure"

    number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_storage_type: Optional[CycleStorageEnumeration] = field(
        default=None,
        metadata={
            "name": "CycleStorageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    covered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
