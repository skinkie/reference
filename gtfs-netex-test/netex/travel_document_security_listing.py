from dataclasses import dataclass, field
from netex.travel_document_security_listing_versioned_child_structure import TravelDocumentSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentSecurityListing(TravelDocumentSecurityListingVersionedChildStructure):
    """
    A listing of a TRAVEL DOCUMENT on a SECURITY LIST.

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
