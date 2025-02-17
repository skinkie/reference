from dataclasses import dataclass

from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfCodespaceAssignmentValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfCodespaceAssignment_ValueStructure"
