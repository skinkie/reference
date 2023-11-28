from dataclasses import dataclass, field
from netex.customer_account_security_listing_versioned_child_structure import CustomerAccountSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountSecurityListing(CustomerAccountSecurityListingVersionedChildStructure):
    """
    A listing of a CUSTOMER ACCOUNT on a SECURITY LIST.

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
