from dataclasses import dataclass, field

from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareContractSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "FareContractSecurityListingRefs_RelStructure"

    fare_contract_security_listing_ref: list[FareContractSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
