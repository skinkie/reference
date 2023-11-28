from dataclasses import dataclass
from netex.medium_access_device_security_listing_ref_structure import MediumAccessDeviceSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDeviceSecurityListingRef(MediumAccessDeviceSecurityListingRefStructure):
    """Reference to a MEDIUM ACCESS DEVICE SECURITY LISTING.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
