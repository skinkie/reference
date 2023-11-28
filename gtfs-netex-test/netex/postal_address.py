from dataclasses import dataclass, field
from netex.postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PostalAddress(PostalAddressVersionStructure):
    """
    A POSTAL ADDRESS to which mail can be sent.

    :ivar id: Identifier of POSTAL ADDRESS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
