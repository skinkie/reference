from dataclasses import dataclass

from .medium_access_device_security_listing_ref_structure import MediumAccessDeviceSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MediumAccessDeviceSecurityListingRef(MediumAccessDeviceSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
