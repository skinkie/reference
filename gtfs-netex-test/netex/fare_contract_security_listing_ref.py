from dataclasses import dataclass

from .fare_contract_security_listing_ref_structure import FareContractSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareContractSecurityListingRef(FareContractSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
