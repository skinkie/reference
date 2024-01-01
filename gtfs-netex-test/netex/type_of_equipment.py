from dataclasses import dataclass
from .type_of_equipment_value_structure import TypeOfEquipmentValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEquipment(TypeOfEquipmentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
