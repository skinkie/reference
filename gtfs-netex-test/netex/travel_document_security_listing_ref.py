from dataclasses import dataclass
from netex.travel_document_security_listing_ref_structure import TravelDocumentSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentSecurityListingRef(TravelDocumentSecurityListingRefStructure):
    """
    Reference to a TRAVEL DOCUMENT SECURITY LISTING..
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
