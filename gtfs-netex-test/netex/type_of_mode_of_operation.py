from dataclasses import dataclass

from .type_of_mode_of_operation_value_structure import TypeOfModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfModeOfOperation(TypeOfModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
