from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_equipment import TypeOfEquipment
from netex.type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfEquipmentRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPE OF Equipment.
    """
    class Meta:
        name = "typesOfEquipment_RelStructure"

    type_of_equipment_ref_or_type_of_equipment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfEquipmentRef",
                    "type": TypeOfEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
