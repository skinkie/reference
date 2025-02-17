from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .travel_document_security_listing_ref import TravelDocumentSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TravelDocumentSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TravelDocumentSecurityListingRefs_RelStructure"

    travel_document_security_listing_ref: list[TravelDocumentSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
