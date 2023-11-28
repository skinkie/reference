from dataclasses import dataclass, field
from netex.medium_access_device_security_listing_versioned_child_structure import MediumAccessDeviceSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDeviceSecurityListing(MediumAccessDeviceSecurityListingVersionedChildStructure):
    """A listing of a MEDIUM ACCESS DEVICE on a SECURITY LIST.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
