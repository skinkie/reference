from dataclasses import dataclass
from netex.extensions_structure_2 import ExtensionsStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Extensions2(ExtensionsStructure2):
    """User defined Extensions to ENTITY in schema.

    (Wrapper tag used to avoid problems with handling of optional 'any'
    by some validators).
    """
    class Meta:
        name = "Extensions"
        namespace = "http://www.netex.org.uk/netex"
