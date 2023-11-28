from dataclasses import dataclass, field
from netex.codespace_assignment_versioned_child_structure import CodespaceAssignmentVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceAssignment(CodespaceAssignmentVersionedChildStructure):
    """
    Assignment of use of a CODESPACE to identify data within a given ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
