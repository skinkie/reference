from dataclasses import dataclass
from netex.extensions_structure_1 import ExtensionsStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class Extensions1(ExtensionsStructure1):
    """Extensions to schema.

    (Wrapper tag used to avoid problems with handling of optional 'any'
    by some validators).
    """
    class Meta:
        name = "Extensions"
        namespace = "http://www.siri.org.uk/siri"
