from dataclasses import dataclass
from netex.retail_device_security_listing_ref_structure import RetailDeviceSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDeviceSecurityListingRef(RetailDeviceSecurityListingRefStructure):
    """
    Reference to a RETAIL DEVICE SECURITY LISTING..
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
