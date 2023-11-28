from dataclasses import dataclass
from netex.type_of_equipment_ref_structure import TypeOfEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfEquipmentRef(TypeOfEquipmentRefStructure):
    """
    Reference to a TYPE OF EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
