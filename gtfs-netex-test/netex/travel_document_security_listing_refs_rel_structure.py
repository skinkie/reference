from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.travel_document_security_listing_ref import TravelDocumentSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TRAVEL DOCUMENT SECURITY LISTING.s.
    """
    class Meta:
        name = "TravelDocumentSecurityListingRefs_RelStructure"

    travel_document_security_listing_ref: List[TravelDocumentSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
