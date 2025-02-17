from dataclasses import dataclass

from .path_instruction_ref_structure import PathInstructionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PathInstructionRef(PathInstructionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
