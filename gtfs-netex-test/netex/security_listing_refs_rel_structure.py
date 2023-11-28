from dataclasses import dataclass, field
from typing import List
from netex.customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from netex.customer_security_listing_ref import CustomerSecurityListingRef
from netex.fare_contract_security_listing_ref import FareContractSecurityListingRef
from netex.medium_access_device_security_listing_ref import MediumAccessDeviceSecurityListingRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from netex.travel_document_security_listing_ref import TravelDocumentSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to SECURITY LISTING.
    """
    class Meta:
        name = "SecurityListingRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TravelDocumentSecurityListingRef",
                    "type": TravelDocumentSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MediumAccessDeviceSecurityListingRef",
                    "type": MediumAccessDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListingRef",
                    "type": RetailDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListingRef",
                    "type": CustomerAccountSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListingRef",
                    "type": FareContractSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListingRef",
                    "type": CustomerSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
