from dataclasses import dataclass
from netex.type_of_security_list_ref_structure import TypeOfSecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfSecurityListRef(TypeOfSecurityListRefStructure):
    """
    Reference to a TYPE OF SECURITY LIST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
