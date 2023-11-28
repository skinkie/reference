from dataclasses import dataclass, field
from typing import List
from netex.customer_security_listing_ref import CustomerSecurityListingRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of CUSTOMER SECURITY LISTING.s.
    """
    class Meta:
        name = "CustomerSecurityListingRefs_RelStructure"

    customer_security_listing_ref: List[CustomerSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
