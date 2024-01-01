from dataclasses import dataclass
from .type_of_codespace_assignment_ref_structure import (
    TypeOfCodespaceAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfCodespaceAssignmentRef(TypeOfCodespaceAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
