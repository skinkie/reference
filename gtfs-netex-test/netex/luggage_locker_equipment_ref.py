from dataclasses import dataclass
from netex.luggage_locker_equipment_ref_structure import LuggageLockerEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageLockerEquipmentRef(LuggageLockerEquipmentRefStructure):
    """
    Identifier of an LUGGAGE LOCKER EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
