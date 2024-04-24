from dataclasses import dataclass

from .path_instruction_versioned_child_structure import PathInstructionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathInstruction(PathInstructionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
