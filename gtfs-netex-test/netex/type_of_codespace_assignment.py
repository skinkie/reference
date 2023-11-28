from dataclasses import dataclass, field
from netex.type_of_codespace_assignment_value_structure import TypeOfCodespaceAssignmentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCodespaceAssignment(TypeOfCodespaceAssignmentValueStructure):
    """
    Classification of an CODESPACE ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
