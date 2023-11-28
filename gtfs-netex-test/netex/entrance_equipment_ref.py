from dataclasses import dataclass
from netex.entrance_equipment_ref_structure import EntranceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntranceEquipmentRef(EntranceEquipmentRefStructure):
    """
    Identifier of an ENTRANCE EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
