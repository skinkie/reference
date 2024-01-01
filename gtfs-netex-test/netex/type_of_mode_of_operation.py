from dataclasses import dataclass
from .type_of_mode_of_operation_value_structure import (
    TypeOfModeOfOperationValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfModeOfOperation(TypeOfModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
