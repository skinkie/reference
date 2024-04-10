from dataclasses import dataclass

from .security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListing1(SecurityListingVersionedChildStructure):
    class Meta:
        name = "SecurityListing"
        namespace = "http://www.netex.org.uk/netex"
