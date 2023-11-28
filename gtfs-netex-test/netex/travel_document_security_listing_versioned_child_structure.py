from dataclasses import dataclass, field
from typing import Optional
from netex.security_listing_versioned_child_structure import SecurityListingVersionedChildStructure
from netex.service_access_code_ref import ServiceAccessCodeRef
from netex.travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    """
    Type for TRAVEL DOCUMENT SECURITY LISTING.
    """
    class Meta:
        name = "TravelDocumentSecurityListing_VersionedChildStructure"

    service_access_code_ref_or_travel_document_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
