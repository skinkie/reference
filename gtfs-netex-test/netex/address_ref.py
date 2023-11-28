from dataclasses import dataclass
from netex.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AddressRef(AddressRefStructure):
    """
    Reference to an ADDRESS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
