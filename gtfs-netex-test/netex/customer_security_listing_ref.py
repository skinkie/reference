from dataclasses import dataclass
from netex.customer_security_listing_ref_structure import CustomerSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerSecurityListingRef(CustomerSecurityListingRefStructure):
    """
    Reference to a CUSTOMER SECURITY LISTING..
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
