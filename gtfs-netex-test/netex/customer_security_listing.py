from dataclasses import dataclass, field
from netex.customer_security_listing_versioned_child_structure import CustomerSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerSecurityListing(CustomerSecurityListingVersionedChildStructure):
    """
    A listing of a CUSTOMER on a SECURITY LIST.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
