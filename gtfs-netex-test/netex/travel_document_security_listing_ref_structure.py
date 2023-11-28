from dataclasses import dataclass
from netex.security_listing_ref_structure import SecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentSecurityListingRefStructure(SecurityListingRefStructure):
    """
    Type for Reference to a TRAVEL DOCUMENT SECURITY LISTING..
    """
