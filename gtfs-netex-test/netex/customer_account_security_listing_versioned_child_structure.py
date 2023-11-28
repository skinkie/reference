from dataclasses import dataclass, field
from typing import Optional
from netex.customer_account_ref import CustomerAccountRef
from netex.security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    """
    Type for CUSTOMER ACCOUNT SECURITY LISTING.
    """
    class Meta:
        name = "CustomerAccountSecurityListing_VersionedChildStructure"

    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
