from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_account_security_listing import CustomerAccountSecurityListing
from netex.customer_security_listing import CustomerSecurityListing
from netex.fare_contract_security_listing import FareContractSecurityListing
from netex.medium_access_device_security_listing import MediumAccessDeviceSecurityListing
from netex.retail_device_security_listing import RetailDeviceSecurityListing
from netex.travel_document_security_listing import TravelDocumentSecurityListing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SecurityListingsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SECURITY LISTINGs.
    """
    class Meta:
        name = "securityListings_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MediumAccessDeviceSecurityListing",
                    "type": MediumAccessDeviceSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentSecurityListing",
                    "type": TravelDocumentSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListing",
                    "type": RetailDeviceSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListing",
                    "type": FareContractSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListing",
                    "type": CustomerSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListing",
                    "type": CustomerAccountSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
