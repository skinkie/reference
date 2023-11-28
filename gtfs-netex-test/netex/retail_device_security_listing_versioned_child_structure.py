from dataclasses import dataclass, field
from typing import Optional
from netex.retail_device_ref import RetailDeviceRef
from netex.security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDeviceSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    """
    Type for  RETAIL DEVICE SECURITY LISTING.
    """
    class Meta:
        name = "RetailDeviceSecurityListing_VersionedChildStructure"

    retail_device_ref: Optional[RetailDeviceRef] = field(
        default=None,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
