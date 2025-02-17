from dataclasses import dataclass

from .codespace_ref_structure import CodespaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CodespaceRef(CodespaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
