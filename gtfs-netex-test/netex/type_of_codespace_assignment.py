from dataclasses import dataclass
from .type_of_codespace_assignment_value_structure import (
    TypeOfCodespaceAssignmentValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCodespaceAssignment(TypeOfCodespaceAssignmentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
