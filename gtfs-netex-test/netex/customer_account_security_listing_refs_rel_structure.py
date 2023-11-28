from dataclasses import dataclass, field
from typing import List
from netex.customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of CUSTOMER ACCOUNT SECURITY LISTING.s.
    """
    class Meta:
        name = "customerAccountSecurityListingRefs_RelStructure"

    customer_account_security_listing_ref: List[CustomerAccountSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
