from dataclasses import dataclass
from netex.security_listing_ref_structure import SecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractSecurityListingRefStructure(SecurityListingRefStructure):
    """
    Type for Reference to a FARE CONTRACT SECURITY LISTING..
    """
