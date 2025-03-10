from dataclasses import dataclass, field

from .customer_security_listing_ref import CustomerSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "CustomerSecurityListingRefs_RelStructure"

    customer_security_listing_ref: list[CustomerSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
