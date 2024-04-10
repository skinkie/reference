from dataclasses import dataclass

from .security_listing_ref_structure import SecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceSecurityListingRefStructure(SecurityListingRefStructure):
    pass
