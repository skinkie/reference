from dataclasses import dataclass, field
from netex.retail_device_security_listing_versioned_child_structure import RetailDeviceSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDeviceSecurityListing(RetailDeviceSecurityListingVersionedChildStructure):
    """
    A listing of a RETAIL DEVICE on a SECURITY LIST.

    :ivar id: Identifier of RETAIL DEVICE SECURITY LISTING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
