from dataclasses import dataclass

from .codespace_structure import CodespaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Codespace(CodespaceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
