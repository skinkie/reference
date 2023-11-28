from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.retail_device_security_listing_ref import RetailDeviceSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDeviceSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of RETAIL DEVICE SECURITY LISTING.s.
    """
    class Meta:
        name = "RetailDeviceSecurityListingRefs_RelStructure"

    retail_device_security_listing_ref: List[RetailDeviceSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
