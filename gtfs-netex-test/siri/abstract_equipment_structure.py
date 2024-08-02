from dataclasses import dataclass, field
from typing import Optional

from .data_managed_object_structure import DataManagedObjectStructure
from .equipment_type_ref_structure import EquipmentTypeRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AbstractEquipmentStructure(DataManagedObjectStructure):
    equipment_id: str = field(
        metadata={
            "name": "EquipmentId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        }
    )
    equipment_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentName",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    type_of_equipment: Optional[EquipmentTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
