from dataclasses import dataclass

from .type_of_equipment_ref_structure import TypeOfEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEquipmentRef(TypeOfEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
