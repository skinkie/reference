from dataclasses import dataclass

from .type_of_mode_of_operation_ref_structure import TypeOfModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfModeOfOperationRef(TypeOfModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
