from dataclasses import dataclass

from .security_listing_ref_structure import SecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SecurityListingRef(SecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
