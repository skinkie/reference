from dataclasses import dataclass
from netex.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PrivateCode(PrivateCodeStructure):
    """A private code that uniquely identifies the element.

    May be used for inter-operating with other (legacy) systems.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
