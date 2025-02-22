from dataclasses import dataclass, field

from .medium_access_device_security_listing_ref import MediumAccessDeviceSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MediumAccessDeviceSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "mediumAccessDeviceSecurityListingRefs_RelStructure"

    medium_access_device_security_listing_ref: list[MediumAccessDeviceSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "MediumAccessDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
