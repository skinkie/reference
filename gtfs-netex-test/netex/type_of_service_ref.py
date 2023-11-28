from dataclasses import dataclass
from netex.type_of_service_ref_structure import TypeOfServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfServiceRef(TypeOfServiceRefStructure):
    """
    Reference to a TYPE OF SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
