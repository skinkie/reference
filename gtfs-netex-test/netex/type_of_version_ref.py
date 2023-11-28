from dataclasses import dataclass
from netex.type_of_version_ref_structure import TypeOfVersionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfVersionRef(TypeOfVersionRefStructure):
    """Reference to a TYPE OF VERSION.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
