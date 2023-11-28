from dataclasses import dataclass
from netex.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PostalAddressRefStructure(AddressRefStructure):
    """
    Type for a reference to a TYPE OF ACTIVATION.
    """
