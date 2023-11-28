from dataclasses import dataclass
from netex.codespace_ref_structure import CodespaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceRef(CodespaceRefStructure):
    """
    Reference to a CODESPACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
