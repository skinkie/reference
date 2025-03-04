from dataclasses import dataclass

from .type_of_equipment_value_structure import TypeOfEquipmentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfEquipment(TypeOfEquipmentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
